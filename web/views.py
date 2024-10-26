from django.shortcuts import render

from .models import Categoria, Producto

"""VISTAS"""

def dashboard ( request ):
    return render( request, 'web/dashboard-admin.html' )

def crear_producto ( request ):
    return render( request, 'web/crear_producto.html' )

def crear_usuario ( request ):
    return render( request, 'web/crear_usuario.html' )

def ingresar_venta ( request ):
    return render( request, 'web/ingresar_venta.html' )

def perfil_usuario ( request ):
    return render( request, 'web/perfil_usuario.html' )

def todas_las_ventas ( request ):
    return render( request, 'web/todas_las_ventas.html' )

def todos_los_productos ( request ):
    listaProductos = Producto.objects.all()
    print(listaProductos)
    context = {
        'productos':listaProductos
    }
    return render( request, 'web/todos_los_productos.html', context )

def todos_los_usuarios ( request ):
    return render( request, 'web/todos_los_usuarios.html' )








