CREATE OR REPLACE PROCEDURE audit.delete_user_data(target_user text)
LANGUAGE plpgsql
AS $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN
        SELECT DISTINCT table_name, record_id, pk_col
        FROM audit.log
        WHERE changed_by = target_user
          AND action = 'INSERT'
          AND record_id IS NOT NULL
    LOOP
        EXECUTE format('DELETE FROM %I WHERE %I = $1', r.table_name, r.pk_col) 
        USING r.record_id;
    END LOOP;
END;
$$;