from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bilbioteca import views

router = DefaultRouter()

router.register(r'paises', views.PaisViewSet, basename='pais')
router.register(r'regiones', views.RegionViewSet, basename='region')
router.register(r'provincias', views.ProvinciaViewSet, basename='provincia')
router.register(r'comunas', views.ComunaViewSet, basename='comuna')
router.register(r'direcciones', views.DireccionViewSet, basename='direccion')
router.register(r'bibliotecas', views.BibliotecaViewSet, basename='biblioteca')
router.register(r'autores', views.AutorViewSet, basename='autor')
router.register(r'generos', views.GeneroViewSet, basename='genero')
router.register(r'subgeneros', views.SubGeneroViewSet, basename='subgenero')
router.register(r'editoriales', views.EditorialViewSet, basename='editorial')
router.register(r'idiomas', views.IdiomaViewSet, basename='idioma')
router.register(r'ediciones', views.EdicionViewSet, basename='edicion')
router.register(r'libros', views.LibroViewSet, basename='libro')
router.register(r'estados', views.EstadoViewSet, basename='estado')
router.register(r'ubicaciones', views.UbicacionViewSet, basename='ubicacion')
router.register(r'inventarios', views.InventarioViewSet, basename='inventario')
router.register(r'usuarios', views.UsuarioViewSet, basename='usuario')
router.register(r'prestamos', views.PrestamoViewSet, basename='prestamo')

urlpatterns = [
    path('api/', include(router.urls)),
]