-- Create a regular app user
CREATE ROLE Admin WITH PASSWORD 'password';
CREATE ROLE ETL WITH PASSWORD 'password';
CREATE ROLE Analyst WITH PASSWORD 'password';
CREATE ROLE Customer WITH PASSWORD 'password';
CREATE ROLE Warehouse WITH PASSWORD 'password';
CREATE ROLE Staff WITH PASSWORD 'password';

CREATE ROLE read_only WITH PASSWORD 'password';
CREATE ROLE read_write WITH PASSWORD 'password';
CREATE ROLE admin with PASSWORD 'password';

CREATE SCHEMA bikestore 

GRANT CONNECT ON DATABASE bikestore_db TO read_only;
GRANT SELECT ON DATABASE bikestore_db TO read_only;


-- Grant privileges only on your app DB
GRANT CONNECT ON DATABASE integrated_db TO app_user;
GRANT CONNECT ON DATABASE 


-- After DB creation, connect and grant table/schema privileges
\c integrated_db;

-- Grant privileges on public schema (if you're using it)
GRANT USAGE ON SCHEMA public TO app_user;
GRANT CREATE ON SCHEMA public TO app_user;

-- Grant permissions on existing objects (if any)
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO app_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO app_user;

-- Ensure future tables created in public belong to app_user
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT SELECT ON TABLES TO app_user;