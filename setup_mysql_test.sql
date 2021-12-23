-- Task 4: MySQL setup test
-- Write a script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
DROP USER IF EXISTS 'hbnb_test'@'localhost';
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
