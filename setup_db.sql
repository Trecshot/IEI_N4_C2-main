-- ==============================================================================
-- Proyecto: API REST Biblioteca (Evaluación N.° 2 - Backend)
-- Motor de Base de Datos: MySQL / MariaDB (XAMPP)
-- Descripción: Script de inicialización de Base de Datos, Usuario y Permisos.
-- ==============================================================================

-- 1. Destruir la base de datos si ya existe (prevención de errores en la corrección)
DROP DATABASE IF EXISTS biblioteca_db;

-- 2. Crear la base de datos con codificación universal para evitar problemas con tildes/ñ
CREATE DATABASE biblioteca_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 3. Crear el usuario del sistema
-- IMPORTANTE: La contraseña 'password_seguro' DEBE ser idéntica a la variable DB_PASSWORD en el archivo .env
CREATE USER IF NOT EXISTS 'biblioteca_user'@'localhost' IDENTIFIED BY 'password_seguro';

-- 4. Asignar todos los privilegios sobre la base de datos al nuevo usuario
GRANT ALL PRIVILEGES ON biblioteca_db.* TO 'biblioteca_user'@'localhost';

-- 5. Refrescar los privilegios del motor para aplicar los cambios inmediatamente
FLUSH PRIVILEGES;
