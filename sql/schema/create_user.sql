-- Create a regular app user
CREATE USER app_user WITH PASSWORD 'password';

-- Grant privileges only on your app DB
GRANT CONNECT ON DATABASE integrated_db TO app_user;

-- After DB creation, connect and grant table/schema privileges
\connect integrated_db;

-- Optional: create a separate schema owned by app_user
CREATE SCHEMA IF NOT EXISTS app AUTHORIZATION app_user;

-- Grant privileges on public schema (if you're using it)
GRANT USAGE ON SCHEMA public TO app_user;
GRANT CREATE ON SCHEMA public TO app_user;

-- Grant permissions on existing objects (if any)
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO app_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO app_user;

-- Ensure future tables created in public belong to app_user
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT ALL ON TABLES TO app_user;