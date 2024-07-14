from django import forms
from .models import Usuario, Producto, Categoria
from django.forms import ModelForm

class UsuarioForm(ModelForm):
    class Meta: 
        model = Usuario
        fields = ["nombre", "correo", "contrasena"] 
        labels = {'contrasena': 'Contraseña'}

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre_producto","precio","cantidad","categoria","imagen"]
        labels = {'nombre_producto': 'Producto'}

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre_categoria"]
        labels = {'nombre_categoria': 'Categoria'}