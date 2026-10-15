from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # Importa RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('bilbioteca.urls')),  # Tu enrutador de la API actual
    
    # Añade esta línea para redirigir la raíz al API
    path('', RedirectView.as_view(url='/api/', permanent=True)),
]
