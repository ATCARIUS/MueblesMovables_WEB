from django.urls import path
from .views import index ,mueblesmovablesproductos,agregarProducto,listarProductos,registro

urlpatterns = [
    path('',index, name='index'),
    path('mueblesmovablesproductos/',mueblesmovablesproductos,name='mueblesmovablesproductos'),
    path('agregarProducto/',agregarProducto, name="agregarProducto"),
    path('listarProductos/',listarProductos, name="listarProductos"),
    path('registro/',registro, name="registro")

]