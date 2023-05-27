from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index, name='index'),
    path('InicioSesion',views.InicioSesion, name='InicioSesion'),
    path('mueblesmovablesproductos',views.mueblesmovablesproductos,name='mueblesmovablesproductos'),
    path('RegistroSesion',views.RegistroSesion , name='RegistroSesion')
]