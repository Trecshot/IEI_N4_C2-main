-- =====================================================================
-- setup_db.sql
-- Script DDL/DCL para la base de datos del proyecto Biblioteca (MySQL).
-- Ejecutar como usuario administrador (root):
--     mysql -u root -p < setup_db.sql
-- Luego aplicar las migraciones:
--     python manage.py migrate
-- =====================================================================

-- DDL: Crear base de datos
CREATE DATABASE IF NOT EXISTS biblioteca_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- DCL: Crear usuario con credenciales exclusivas
CREATE USER IF NOT EXISTS 'biblioteca_user'@'localhost' IDENTIFIED BY 'password_seguro_123';

-- DCL: Asignar permisos sobre la base de datos
GRANT ALL PRIVILEGES ON biblioteca_db.* TO 'biblioteca_user'@'localhost';

FLUSH PRIVILEGES;


-- =====================================================================
-- Alternativa PostgreSQL (ejecutar con: psql -U postgres -f setup_db.sql)
-- =====================================================================
-- CREATE DATABASE biblioteca_db;
-- CREATE USER biblioteca_user WITH PASSWORD 'password_seguro_123';
-- GRANT ALL PRIVILEGES ON DATABASE biblioteca_db TO biblioteca_user;
-- \c biblioteca_db
-- GRANT ALL ON SCHEMA public TO biblioteca_user;  -- requerido en PostgreSQL 15+
