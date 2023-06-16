from django.urls import path
from .views import index , InicioSesion,mueblesmovablesproductos,RegistroSesion,agregarProducto,listarProductos

urlpatterns = [
    path('',index, name='index'),
    path('InicioSesion/',InicioSesion, name='InicioSesion'),
    path('mueblesmovablesproductos/',mueblesmovablesproductos,name='mueblesmovablesproductos'),
    path('RegistroSesion/',RegistroSesion , name='RegistroSesion'),
    path('agregarProducto/',agregarProducto, name="agregarProducto"),
        path('listarProductos/',listarProductos, name="listarProductos")
]