from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Usuario, Producto, Categoria
from .forms import CategoriaForm, ProductoForm, UsuarioForm
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def inicio(request):
    context={}
    return render(request, 'AplicacionPlantas/inicio.html', context)

def carrodecompras(request):
    context={}
    return render(request, 'AplicacionPlantas/Carrodecompras.html', context)

def iniciosesion(request):
    context={}
    return render(request, 'AplicacionPlantas/Iniciosesion.html', context)

def donaciones(request):
    context={}
    return render(request, 'AplicacionPlantas/Donaciones.html', context)

def productos(request):
    context={}
    return render(request, 'AplicacionPlantas/Productos.html', context)

def productossemillas(request):
    context={}
    return render(request, 'AplicacionPlantas/Productossemillas.html', context)

def productostierra(request):
    context={}
    return render(request, 'AplicacionPlantas/Productostierra.html', context)

def crud_categorias(request):

    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    print("Enviando datos categorias_list")
    return render(request, 'AplicacionPlantas/categorias_list.html', context)

def categoriasAdd(request):
    print("Estoy controlando categoriasAdd...")
    context={}

    if request.method == "POST":
        print("Controlador es un post...")
        form = CategoriaForm(request.POST)

        if form.is_valid:
            print("Estoy en agregar, is_valid")
            form.save()

            #limpiar forms
            form=CategoriaForm()

            context = {'mensaje':"Ok, datos grabados...", "form":form}
            return render(request, 'AplicacionPlantas/categorias_add.html',context)
        else:
            context = {'form':form}
    else:
        form = CategoriaForm()
        context = {'form':form}
        return render(request, 'AplicacionPlantas/categorias_add.html',context)

def categorias_del(request, pk):
    mensajes = []
    errores = []
    context = {}

    try:
        categoria = Categoria.objects.get(id_categoria=pk)
        categoria.delete()
        mensajes.append("Bien, datos eliminados...")
    except Categoria.DoesNotExist:
        errores.append("Error, id no existe")
    except Exception as e:
        errores.append(f"Error inesperado: {str(e)}")

    categorias = Categoria.objects.all()
    context = {'categorias': categorias, 'mensajes': mensajes, 'errores': errores}
    return render(request, 'AplicacionPlantas/categorias_list.html', context)


def categorias_edit(request,pk):
    try:
        categoria = Categoria.objects.get(id_categoria=pk)
        context = {}
        if categoria:
            print("Edit encontro el categoria...")
            if request.method == "POST":
                print("Edit, es un POST")
                form = CategoriaForm(request.POST, instance=categoria)
                form.save()
                mensaje = "Bien, datos actualizados..."
                print(mensaje)
                context = {'categoria':categoria, 'form':form, 'mensaje':mensaje}
                return render(request, 'AplicacionPlantas/categorias_edit.html', context)
            else:
                # no es un POST
                print("Edit, NO es un POST")
                form = CategoriaForm(instance=categoria)
                mensaje = ""
                context = {'categoria':categoria, 'form':form, 'mensaje':mensaje}
                return render(request, 'AplicacionPlantas/categorias_edit.html', context)
    except:
        print("Error, id no existe...")
        categorias = Categoria.objects.all()
        mensaje = "Error, id no existe"
        context = {'mensaje':mensaje, 'categorias':categorias}
        return render(request, 'AplicacionPlantas/categorias_list.html', context)
    
# PRODUCTOS

def crud_productos(request):

    productos = Producto.objects.all()
    context = {'productos': productos}
    print("Enviando datos categorias_list")
    return render(request, 'AplicacionPlantas/productos_list.html', context)

def productosAdd(request):
    print("Estoy controlando categoriasAdd...")
    context={}

    if request.method == "POST":
        print("Controlador es un post...")
        form = ProductoForm(request.POST)

        if form.is_valid:
            print("Estoy en agregar, is_valid")
            form.save()

            #limpiar forms
            form=ProductoForm()

            context = {'mensaje':"Ok, datos grabados...", "form":form}
            return render(request, 'AplicacionPlantas/productos_add.html',context)
        else:
            context = {'form':form}
    else:
        form = ProductoForm()
        context = {'form':form}
        return render(request, 'AplicacionPlantas/productos_add.html',context)

def productos_del(request, pk):
    mensajes = []
    errores = []
    context = {}

    try:
        producto = Producto.objects.get(id_producto=pk)
        producto.delete()
        mensajes.append("Bien, datos eliminados...")
    except Categoria.DoesNotExist:
        errores.append("Error, id no existe")
    except Exception as e:
        errores.append(f"Error inesperado: {str(e)}")

    productos = Producto.objects.all()
    context = {'productos': productos, 'mensajes': mensajes, 'errores': errores}
    return render(request, 'AplicacionPlantas/productos_list.html', context)


def productos_edit(request,pk):
    try:
        producto = Producto.objects.get(id_producto=pk)
        context = {}
        if producto:
            print("Edit encontro el producto...")
            if request.method == "POST":
                print("Edit, es un POST")
                form = ProductoForm(request.POST, instance=producto)
                form.save()
                mensaje = "Bien, datos actualizados..."
                print(mensaje)
                context = {'producto':producto, 'form':form, 'mensaje':mensaje}
                return render(request, 'AplicacionPlantas/productos_edit.html', context)
            else:
                # no es un POST
                print("Edit, NO es un POST")
                form = ProductoForm(instance=producto)
                mensaje = ""
                context = {'producto':producto, 'form':form, 'mensaje':mensaje}
                return render(request, 'AplicacionPlantas/productos_edit.html', context)
    except:
        print("Error, id no existe...")
        producto = Producto.objects.all()
        mensaje = "Error, id no existe"
        context = {'mensaje':mensaje, 'productos':productos}
        return render(request, 'AplicacionPlantas/productos_list.html', context)
    
#USUARIOS

def crud_usuarios(request):

    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios}
    print("Enviando datos usuarios_list")
    return render(request, 'AplicacionPlantas/usuarios_list.html', context)

def usuariosAdd(request):
    print("Estoy controlando usuariosAdd...")
    context={}

    if request.method == "POST":
        print("Controlador es un post...")
        form = UsuarioForm(request.POST)

        if form.is_valid:
            print("Estoy en agregar, is_valid")
            form.save()

            #limpiar forms
            form=UsuarioForm()

            context = {'mensaje':"Ok, datos grabados...", "form":form}
            return render(request, 'AplicacionPlantas/usuarios_add.html',context)
        else:
            context = {'form':form}
    else:
        form = UsuarioForm()
        context = {'form':form}
        return render(request, 'AplicacionPlantas/usuarios_add.html',context)

def usuarios_del(request, pk):
    mensajes = []
    errores = []
    context = {}

    try:
        usuario = Usuario.objects.get(id_usuario=pk)
        usuario.delete()
        mensajes.append("Bien, datos eliminados...")
    except Usuario.DoesNotExist:
        errores.append("Error, id no existe")
    except Exception as e:
        errores.append(f"Error inesperado: {str(e)}")

    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios, 'mensajes': mensajes, 'errores': errores}
    return render(request, 'AplicacionPlantas/usuarios_list.html', context)


def usuarios_edit(request,pk):
    try:
        usuario = Usuario.objects.get(id_usuario=pk)
        context = {}
        if usuario:
            print("Edit encontro el usuario...")
            if request.method == "POST":
                print("Edit, es un POST")
                form = UsuarioForm(request.POST, instance=usuario)
                form.save()
                mensaje = "Bien, datos actualizados..."
                print(mensaje)
                context = {'usuario':usuario, 'form':form, 'mensaje':mensaje}
                return render(request, 'AplicacionPlantas/usuarios_edit.html', context)
            else:
                # no es un POST
                print("Edit, NO es un POST")
                form = UsuarioForm(instance=usuario)
                mensaje = ""
                context = {'usuario':usuario, 'form':form, 'mensaje':mensaje}
                return render(request, 'AplicacionPlantas/usuarios_edit.html', context)
    except:
        print("Error, id no existe...")
        usuarios = Usuario.objects.all()
        mensaje = "Error, id no existe"
        context = {'mensaje':mensaje, 'usuarios':usuarios}
        return render(request, 'AplicacionPlantas/usuarios_list.html', context)
    
#REGISTRO

def acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=password)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, F"Bienvenid@ de nuevo {nombre_usuario}")
                return redirect("blog")
            else:
                messages.error(request, "Los datos son incorrectos")
        else:
            messages.error(request, "Los datos son incorrectos")

    form = AuthenticationForm()
    return render(request, "acceder.html", {"form": form})

class VistaRegistro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro.html", {"form": form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get("username")
            messages.success(request, F"Bienvenid@ a la plataforma {nombre_usuario}")
            login(request, usuario)
            return redirect("blog")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro.html", {"form": form})
        

def salir(request):
    logout(request)
    messages.success(request, F"Tu sesión se ha cerrado correctamente")
    return redirect("acceder")



    
    