from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_comerciales, name='lista_comerciales'), 
    path('crear/', views.crear_comercial, name='crear_comercial'),
    path('editar/<str:id>/', views.editar_comercial, name='editar_comercial'),
    path('eliminar/<str:id>/', views.eliminar_comercial, name='eliminar_comercial'),
    
    ]
