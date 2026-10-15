from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PaisViewSet,
    RegionViewSet,
    ProvinciaViewSet,
    ComunaViewSet,
    DireccionViewSet,
    BibliotecaViewSet,
    AutorViewSet,
    GeneroViewSet,
    SubGeneroViewSet,
    EditorialViewSet,
    IdiomaViewSet,
    EdicionViewSet,
    LibroViewSet,
    EstadoViewSet,
    UbicacionViewSet,
    InventarioViewSet,
    UsuarioViewSet,
    PrestamoViewSet,
)

# 4.3 Genera correctamente su archivo urls y las urls para las vistas de su modelo
router = DefaultRouter()
router.register(r'paises', PaisViewSet, basename='pais')
router.register(r'regiones', RegionViewSet, basename='region')
router.register(r'provincias', ProvinciaViewSet, basename='provincia')
router.register(r'comunas', ComunaViewSet, basename='comuna')
router.register(r'direcciones', DireccionViewSet, basename='direccion')
router.register(r'bibliotecas', BibliotecaViewSet, basename='biblioteca')
router.register(r'autores', AutorViewSet, basename='autor')
router.register(r'generos', GeneroViewSet, basename='genero')
router.register(r'subgeneros', SubGeneroViewSet, basename='subgenero')
router.register(r'editoriales', EditorialViewSet, basename='editorial')
router.register(r'idiomas', IdiomaViewSet, basename='idioma')
router.register(r'ediciones', EdicionViewSet, basename='edicion')
router.register(r'libros', LibroViewSet, basename='libro')
router.register(r'estados', EstadoViewSet, basename='estado')
router.register(r'ubicaciones', UbicacionViewSet, basename='ubicacion')
router.register(r'inventarios', InventarioViewSet, basename='inventario')
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'prestamos', PrestamoViewSet, basename='prestamo')

# 4.4 Integra las urls de sus vistas con Django
urlpatterns = [
    path('', include(router.urls)),
]