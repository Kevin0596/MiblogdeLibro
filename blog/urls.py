from django.urls import path
from . import views
from django.urls import path
from .views import about_view

urlpatterns = [
    path('', views.home, name='home'),
    path('autor/', views.agregar_autor, name='agregar_autor'),
    path('categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('post/', views.agregar_post, name='agregar_post'),
    path('buscar/', views.buscar_post, name='buscar_post'),
    path('about/', about_view, name='about'),
]
