from rest_framework import viewsets

from .models import (
    Pais,
    Region,
    Provincia,
    Comuna,
    Direccion,
    Biblioteca,
    Autor,
    Genero,
    SubGenero,
    Editorial,
    Idioma,
    Edicion,
    Libro,
    Estado,
    Ubicacion,
    Inventario,
    Usuario,
    Prestamo,
)

from .serializer import (
    PaisSerializer,
    RegionSerializer,
    ProvinciaSerializer,
    ComunaSerializer,
    DireccionSerializer,
    BibliotecaSerializer,
    AutorSerializer,
    GeneroSerializer,
    SubGeneroSerializer,
    EditorialSerializer,
    IdiomaSerializer,
    EdicionSerializer,
    LibroSerializer,
    EstadoSerializer,
    UbicacionSerializer,
    InventarioSerializer,
    UsuarioSerializer,
    PrestamoSerializer,
)

# 4.2 Genera sus ModelViewSet para su modelo de datos completo
class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class SubGeneroViewSet(viewsets.ModelViewSet):
    queryset = SubGenero.objects.all()
    serializer_class = SubGeneroSerializer

class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

class IdiomaViewSet(viewsets.ModelViewSet):
    queryset = Idioma.objects.all()
    serializer_class = IdiomaSerializer

class EdicionViewSet(viewsets.ModelViewSet):
    queryset = Edicion.objects.all()
    serializer_class = EdicionSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer