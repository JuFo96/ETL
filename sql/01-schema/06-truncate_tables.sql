CREATE OR REPLACE PROCEDURE bikestore.truncate_data_tables()
LANGUAGE plpgsql
AS $$
BEGIN
    TRUNCATE TABLE bikestore.brands CASCADE;
    TRUNCATE TABLE bikestore.categories CASCADE;
    TRUNCATE TABLE bikestore.customers CASCADE;
    TRUNCATE TABLE bikestore.order_items CASCADE;
    TRUNCATE TABLE bikestore.orders CASCADE;
    TRUNCATE TABLE bikestore.products CASCADE;
    TRUNCATE TABLE bikestore.staffs CASCADE;
    TRUNCATE TABLE bikestore.stocks CASCADE;
    TRUNCATE TABLE bikestore.stores CASCADE;

    DELETE FROM audit.log WHERE changed_by = 'etl_app';
END;
$$;