-- setup_db.sql

-- 1. Crear la base de datos
CREATE DATABASE biblioteca_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 2. Crear el usuario (Asegúrese de cambiar 'password_seguro' por el definido en su .env)
CREATE USER 'biblioteca_user'@'localhost' IDENTIFIED BY 'password_seguro';

-- 3. Asignar los permisos sobre la base de datos
GRANT ALL PRIVILEGES ON biblioteca_db.* TO 'biblioteca_user'@'localhost';
FLUSH PRIVILEGES;
