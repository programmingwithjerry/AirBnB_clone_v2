-- this script sets up a MySQL server for the project
-- create a test database for the project named: hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create a new user called: hbnb_test with full privileges on the hbnb_test_db database
-- and the password: hbnb_test_pwd if the user doesn't already exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant the SELECT privilege to the user hbnb_test on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- grant all privileges to the new user on the hbnb_test_db database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

