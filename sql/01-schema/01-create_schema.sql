CREATE SCHEMA bikestore AUTHORIZATION admin;
CREATE SCHEMA audit AUTHORIZATION admin;


CREATE ROLE customer_role;
CREATE ROLE analyst_role;
CREATE ROLE staff_role;
CREATE ROLE admin_role;
CREATE ROLE app_user;

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA bikestore FROM PUBLIC;
REVOKE ALL ON SCHEMA audit FROM PUBLIC;

GRANT USAGE ON SCHEMA bikestore TO customer_role, analyst_role, staff_role, admin_role, app_user;
GRANT USAGE ON SCHEMA audit TO admin_role, app_user;






