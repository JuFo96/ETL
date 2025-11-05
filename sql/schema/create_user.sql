CREATE ROLE read_only WITH PASSWORD 'password';
CREATE ROLE read_write WITH PASSWORD 'password';


-- Read only 
GRANT CONNECT ON DATABASE bikestore_db TO read_only;
CREATE SCHEMA bikestore AUTHORIZATION admin;
GRANT USAGE ON SCHEMA bikestore TO read_only;
GRANT SELECT ON ALL TABLES IN SCHEMA bikestore TO read_only;
ALTER DEFAULT PRIVILEGES FOR ROLE admin IN SCHEMA bikestore 
    GRANT SELECT ON TABLES to read_only;

-- Read Write
GRANT read_only TO read_write;
GRANT INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA bikestore TO read_write;
ALTER DEFAULT PRIVILEGES FOR ROLE admin IN SCHEMA bikestore 
    GRANT INSERT, UPDATE, DELETE ON TABLES TO read_write;
ALTER DEFAULT PRIVILEGES FOR ROLE admin IN SCHEMA bikestore
    GRANT USAGE, SELECT, UPDATE ON SEQUENCES TO read_write;


-- Create a regular app user
CREATE USER etl_app WITH PASSWORD 'password' IN ROLE read_write;
CREATE USER analyst WITH PASSWORD 'password' IN ROLE read_only;
CREATE USER customer WITH PASSWORD 'password' IN ROLE read_only;
CREATE USER warehouse WITH PASSWORD 'password' IN ROLE read_write;
CREATE USER staff WITH PASSWORD 'password' IN ROLE read_only;