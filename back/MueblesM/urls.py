from django.urls import path
from .views import index , InicioSesion,mueblesmovablesproductos,RegistroSesion

urlpatterns = [
    path('',index, name='index'),
    path('InicioSesion/',InicioSesion, name='InicioSesion'),
    path('mueblesmovablesproductos/',mueblesmovablesproductos,name='mueblesmovablesproductos'),
    path('RegistroSesion/',RegistroSesion , name='RegistroSesion')
]