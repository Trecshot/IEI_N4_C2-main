# IEI_N4_C2 – Backend Biblioteca con Django

API REST para la gestión de una biblioteca, construida con **Django**, **Django REST Framework** y **MySQL**.

## Estructura

| Carpeta / archivo | Descripción |
| --- | --- |
| `django_core/` | Configuración del proyecto (`settings.py`, `urls.py`) |
| `bilbioteca/` | Aplicación: modelos, serializers, vistas, rutas, fixtures y templates |
| `setup_db.sql` | Script SQL para crear la base de datos, el usuario y sus permisos |
| `.env.example` | Plantilla de variables de entorno |
| `requirements.txt` | Dependencias del proyecto |

## Instalación rápida

```powershell
# 1. Crear y activar el ambiente virtual
python -m venv nombre_ambiente
.\nombre_ambiente\Scripts\Activate
# Si PowerShell bloquea la activación:
Set-ExecutionPolicy Bypass -Scope CurrentUser

# 2. Instalar dependencias
python -m pip install --upgrade pip
pip install -r requirements.txt

# 3. Crear el archivo de entorno y completar los valores
copy .env.example .env

# 4. Crear base de datos y usuario (como root)
mysql -u root -p < setup_db.sql

# 5. Aplicar migraciones y cargar datos iniciales
python manage.py migrate
python manage.py loaddata data_paises data_regiones data_provincias data_comunas genero

# 6. Crear administrador e iniciar el servidor
python manage.py createsuperuser
python manage.py runserver
```

> [!IMPORTANT]
> El archivo `.env` contiene credenciales (`SECRET_KEY`, contraseña de la DB) y **nunca debe subirse** al repositorio; ya está en `.gitignore`.

## Variables de entorno (`.env`)

```env
DEBUG=True
SECRET_KEY=su_secret_key
DB_NAME=biblioteca_db
DB_USER=biblioteca_user
DB_PASSWORD=password_seguro_123
DB_HOST=localhost
DB_PORT=3306
```

Se leen en `settings.py` con **django-environ**:

```python
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
SECRET_KEY = env('SECRET_KEY')
```

## API REST

Cada modelo expone un CRUD completo (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) mediante `ModelViewSet` y `DefaultRouter`.

- Raíz de la API: http://127.0.0.1:8000/bilbioteca/api/
- Admin de Django: http://127.0.0.1:8000/admin/

Endpoints: `paises`, `regiones`, `provincias`, `comunas`, `direcciones`, `bibliotecas`, `autores`, `generos`, `subgeneros`, `editoriales`, `idiomas`, `ediciones`, `libros`, `estados`, `ubicaciones`, `inventarios`, `usuarios`, `prestamos`.

Ejemplo: `GET /bilbioteca/api/regiones/` lista las regiones y `GET /bilbioteca/api/regiones/1/` obtiene una.

Flujo para agregar un nuevo recurso:
1. Modelo en `models.py` → `python manage.py makemigrations` y `python manage.py migrate`
2. Serializer en `serializer.py` (`fields = '__all__'`)
3. `ModelViewSet` en `views.py`
4. `router.register(...)` en `bilbioteca/urls.py`

## Comandos útiles

| Comando | Uso |
| --- | --- |
| `python manage.py runserver` | Inicia el servidor en http://127.0.0.1:8000 |
| `python manage.py makemigrations` | Genera migraciones tras cambiar los modelos |
| `python manage.py migrate` | Aplica las migraciones a la DB |
| `python manage.py loaddata <fixture>` | Carga datos iniciales desde `bilbioteca/fixtures/` |
| `python manage.py createsuperuser` | Crea un usuario administrador |
| `pip freeze > requirements.txt` | Actualiza la lista de dependencias tras instalar una librería |
| `deactivate` | Desactiva el ambiente virtual |

> [!NOTE]
> Con `DEBUG=False` Django muestra la plantilla `404.html` en vez de información del servidor; los archivos estáticos requieren `python manage.py collectstatic` o `runserver --insecure`.