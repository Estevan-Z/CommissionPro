from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_ventas, name='lista_ventas'),
    path('crear/', views.crear_venta, name='crear_venta'),
]
