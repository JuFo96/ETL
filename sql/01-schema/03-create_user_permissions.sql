SET search_path to bikestore;

-- Customer role 
GRANT SELECT ON customers, orders, order_items TO customer_role;

-- Analyst role 
GRANT SELECT ON ALL TABLES IN SCHEMA bikestore TO analyst_role;


-- Staff role
GRANT SELECT ON ALL TABLES IN SCHEMA bikestore TO staff_role;
GRANT INSERT, UPDATE ON orders, order_items, stocks, customers TO staff_role;

-- Admin role 
GRANT ALL ON ALL TABLES IN SCHEMA bikestore TO admin_role;
GRANT ALL ON ALL TABLES IN SCHEMA audit TO admin_role;

-- App user 
GRANT SELECT, INSERT, UPDATE, DELETE, TRUNCATE ON ALL TABLES IN SCHEMA bikestore TO app_user;
GRANT SELECT, INSERT, DELETE ON audit.log TO app_user;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA bikestore TO app_user;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA audit TO app_user;


CREATE USER etl_app WITH PASSWORD 'password';
GRANT app_user TO etl_app;

CREATE USER admin_user WITH PASSWORD 'password';
GRANT admin_role TO admin_user;