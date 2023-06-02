from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'MueblesM/index.html')

def InicioSesion(request):

    return render(request,'MueblesM/InicioSesion.html')


def mueblesmovablesproductos(request):

    return render(request,'MueblesM/mueblesmovablesproductos.html')


def RegistroSesion(request):

    return render(request ,'MueblesM/RegistroSesion.html')
