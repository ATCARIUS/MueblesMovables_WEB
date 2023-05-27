from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'MueblesM/index.html', context)

def InicioSesion(request):
    context={}
    return render(request,'MueblesM/InicioSesion.html', context)


def mueblesmovablesproductos(request):
    context={}
    return render(request,'MueblesM/mueblesmovablesproductos.html', context)


def RegistroSesion(request):
    context={}
    return render(request ,'MueblesM/RegistroSesion.html', context)