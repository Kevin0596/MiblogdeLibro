from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('autor/', views.agregar_autor, name='agregar_autor'),
    path('categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('post/', views.agregar_post, name='agregar_post'),
    path('buscar/', views.buscar_post, name='buscar_post'),
]
