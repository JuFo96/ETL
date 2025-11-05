

CREATE ROLE read_only WITH PASSWORD 'password';
CREATE ROLE read_write WITH PASSWORD 'password';
CREATE ROLE schema_admin with PASSWORD 'password';

-- Read only 
GRANT CONNECT ON DATABASE bikestore_db TO read_only;
CREATE SCHEMA bikestore AUTHORIZATION schema_admin;
GRANT USAGE ON SCHEMA bikestore TO read_only;
GRANT SELECT ON ALL TABLES IN SCHEMA bikestore TO read_only;

-- Read Write
GRANT read_only TO read_write;
GRANT INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA bikestore TO read_write;


-- Create a regular app user
CREATE USER etl_app WITH PASSWORD 'password' IN ROLE read_write;
CREATE ROLE Analyst WITH PASSWORD 'password' IN ROLE read_only;
CREATE ROLE Customer WITH PASSWORD 'password' IN ROLE read_only;
CREATE ROLE Warehouse WITH PASSWORD 'password' IN ROLE read_write;
CREATE ROLE Staff WITH PASSWORD 'password' IN ROLE read_only;