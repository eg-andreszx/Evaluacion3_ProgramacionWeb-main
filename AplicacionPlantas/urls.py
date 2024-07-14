from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import VistaRegistro, acceder, salir

urlpatterns = [
    path('Inicio.html', views.inicio, name='inicio'),
    path('Carrodecompras.html', views.carrodecompras, name='carrodecompras'),
    path('Donaciones.html', views.donaciones, name='donaciones'),
    path('Iniciosesion.html', views.iniciosesion, name='iniciosesion'),
    path('Productos.html', views.productos, name='productos'),
    path('Productossemillas.html', views.productossemillas, name='productossemillas'),
    path('Productostierra.html', views.productostierra, name='productostierra'),


    # CATEGORIAS
        
    path('crud_categorias', views.crud_categorias, name='crud_categorias'),
    path('categoriasAdd', views.categoriasAdd, name='categoriasAdd'),
    path('categorias_del/<str:pk>', views.categorias_del, name='categorias_del'),
    path('categorias_edit/<str:pk>', views.categorias_edit, name= 'categorias_edit'),

    # PRODUCTOS

    path('crud_productos', views.crud_productos, name='crud_productos'),
    path('productosAdd', views.productosAdd, name='productosAdd'),
    path('productos_del/<str:pk>', views.productos_del, name='productos_del'),
    path('productos_edit/<str:pk>', views.productos_edit, name= 'productos_edit'),

      # USUARIO

    path('crud_usuarios', views.crud_usuarios, name='crud_usuarios'),
    path('usuariosAdd', views.usuariosAdd, name='usuariosAdd'),
    path('usuarios_del/<str:pk>', views.usuarios_del, name='usuarios_del'),
    path('usuarios_edit/<str:pk>', views.usuarios_edit, name= 'usuarios_edit'),

    #REGISTRO

    path('registro/', VistaRegistro.as_view(), name='registro'),
    path('acceder.html/', acceder, name='acceder'),
    path('salir/', salir, name='salir')
    
]