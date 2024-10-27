from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('crear_producto', crear_producto, name='crear_producto'),
    path('crear_usuario', crear_usuario, name='crear_usuario'),
    path('ingresar_venta', ingresar_venta, name='ingresar_venta'),
    path('perfil_usuario', perfil_usuario, name='perfil_usuario'),
    path('todas_las_ventas', todas_las_ventas, name='todas_las_ventas'),
    path('todos_los_productos', todos_los_productos, name='todos_los_productos'),
    path('productos_por_categoria/<int:categoria_id>', productos_por_categoria, name='productos_por_categoria'),
    path('productos_por_nombre', productos_por_nombre, name='productos_por_nombre'),
    path('todos_los_usuarios', todos_los_usuarios, name='todos_los_usuarios'),
]




