from django.shortcuts import render, redirect,get_object_or_404
from .forms import ProductoForm,Mueble

# Create your views here.

def index(request):

    return render(request, 'MueblesM/index.html')

def InicioSesion(request):

    return render(request,'MueblesM/InicioSesion.html')


def mueblesmovablesproductos(request):

    return render(request,'MueblesM/mueblesmovablesproductos.html')


def RegistroSesion(request):

    return render(request ,'MueblesM/RegistroSesion.html')


def agregarProducto(request):

    data = {
        'form': ProductoForm()

    }
    if request.method ==  'POST':
        formulario = ProductoForm(data=request.POST, files=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'MueblesM/muebles/agregar.html',data)


def listarProductos(request):

    productos = Mueble.objects.all()

    data = {
        'productos': productos
    }
    return render(request, 'MueblesM/muebles/listar.html',data)