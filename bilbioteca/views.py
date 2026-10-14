from django.shortcuts import render
from rest_framework import viewsets

from .models import Pais
from .models import Region
from .models import Provincia
from .models import Comuna
from .models import Direccion
from .models import Biblioteca
from .models import Autor
from .models import Genero
from .models import SubGenero
from .models import Editorial
from .models import Idioma
from .models import Edicion
from .models import Libro
from .models import Estado
from .models import Ubicacion
from .models import Inventario
from .models import Usuario
from .models import Prestamo

from .serializer import PaisSerializer
from .serializer import RegionSerializer
from .serializer import ProvinciaSerializer
from .serializer import ComunaSerializer
from .serializer import DireccionSerializer
from .serializer import BibliotecaSerializer
from .serializer import AutorSerializer
from .serializer import GeneroSerializer
from .serializer import SubGeneroSerializer
from .serializer import EditorialSerializer
from .serializer import IdiomaSerializer
from .serializer import EdicionSerializer
from .serializer import LibroSerializer
from .serializer import EstadoSerializer
from .serializer import UbicacionSerializer
from .serializer import InventarioSerializer
from .serializer import UsuarioSerializer
from .serializer import PrestamoSerializer

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

# ModelViewSet genera automáticamente GET (list/retrieve), POST, PUT, PATCH y DELETE

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