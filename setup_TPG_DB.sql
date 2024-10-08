-- prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS tpg_dev_db;
CREATE USER IF NOT EXISTS 'tpg_dev'@'localhost' IDENTIFIED BY 'Tpg@12_34';
GRANT ALL PRIVILEGES ON `tpg_dev_db`.* TO 'tpg_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'tpg_dev'@'localhost';
FLUSH PRIVILEGES;
