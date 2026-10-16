DROP DATABASE IF EXISTS biblioteca_db;
CREATE DATABASE biblioteca_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'biblioteca_user'@'localhost' IDENTIFIED BY 'password_seguro';

GRANT ALL PRIVILEGES ON biblioteca_db.* TO 'biblioteca_user'@'localhost';

FLUSH PRIVILEGES;
