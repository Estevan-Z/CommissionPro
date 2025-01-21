from django.contrib import admin
from django.urls import path, include
from .views import homepage  # Importa la vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comerciales/', include('comerciales.urls')), 
    path('productos/', include('productos.urls')),    
    path('ventas/', include('ventas.urls')),          
    path('', homepage, name='homepage'),             
]
