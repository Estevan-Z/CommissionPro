from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_productos, name='lista_productos'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('eliminar/<str:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('editar/<str:id>/', views.editar_producto, name='editar_producto'),
]
