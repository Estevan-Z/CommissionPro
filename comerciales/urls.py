from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_comerciales, name='lista_comerciales'), 
    path('crear/', views.crear_comercial, name='crear_comercial'),
]
