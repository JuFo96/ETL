CREATE OR REPLACE FUNCTION audit.log_changes()
RETURNS TRIGGER AS $$
DECLARE
    primary_key_column_name text;
    row_data jsonb;
    primary_key_value bigint;
BEGIN
    -- Decide whether to use OLD or NEW depending on the operation
    IF TG_OP = 'INSERT' THEN
        row_data := to_jsonb(NEW);
    ELSE
        row_data := to_jsonb(OLD);
    END IF;

    -- Dynamically determine which column is the primary key
    SELECT col.attname
    INTO primary_key_column_name
    FROM pg_index AS idx
    JOIN pg_attribute AS col
      ON col.attrelid = idx.indrelid
      AND col.attnum = ANY(idx.indkey)
    WHERE idx.indrelid = TG_RELID
      AND idx.indisprimary
    LIMIT 1;

    -- Extract the primary key value from the row data
    IF primary_key_column_name IS NOT NULL THEN
        primary_key_value := (row_data ->> primary_key_column_name)::bigint;
    END IF;

    -- Write audit record
    INSERT INTO audit.log (
        table_name,
        record_id,
        pk_col,
        action,
        changed_by
    )
    VALUES (
        TG_TABLE_SCHEMA || '.' || TG_TABLE_NAME,
        primary_key_value,
        primary_key_column_name,
        TG_OP,
        session_user::text
    );

    RETURN COALESCE(NEW, OLD);
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;


-- Loops over all tables in the bikestore schema and adds the trigger function
DO $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN
        SELECT tablename
        FROM pg_tables
        WHERE schemaname = 'bikestore'
    LOOP
        EXECUTE format('
            DROP TRIGGER IF EXISTS audit_trigger ON bikestore.%I;
            CREATE TRIGGER audit_trigger
            AFTER INSERT OR UPDATE OR DELETE ON bikestore.%I
            FOR EACH ROW EXECUTE FUNCTION audit.log_changes();
        ', r.tablename, r.tablename);
    END LOOP;
END;
$$;