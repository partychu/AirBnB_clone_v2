-- Task 3: MySQL setup development
-- Write a script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
DROP USER IF EXISTS 'hbnb_dev'@'localhost';
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
