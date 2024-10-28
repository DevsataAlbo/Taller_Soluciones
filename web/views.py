from django.shortcuts import render, get_object_or_404

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
    listaCategorias = Categoria.objects.all()

    # print(listaProductos)
    context = {
        'productos':listaProductos,
        'categorias':listaCategorias
    }
    return render( request, 'web/todos_los_productos.html', context )

def productos_por_categoria ( request, categoria_id ):
    # Recupera la categoría seleccionada
    categoria = Categoria.objects.get(id=categoria_id)
    # Obtiene los productos que pertenecen a esta categoría
    productos = Producto.objects.filter(categoria=categoria)
    context = {
        'productos': productos,
        'categoria': categoria
    }
    return render(request, 'web/todos_los_productos.html', context)

def productos_por_nombre ( request ):

    nombre = request.POST['nombre']

    listaProductos = Producto.objects.filter(nombre__contains=nombre)
    listaCategorias = Categoria.objects.all()

    context = {
        'productos': listaProductos,
        'categoria': listaCategorias
    }
    return render(request, 'web/todos_los_productos.html', context)

def producto_detalle ( request,producto_id ):
    # objProducto = Producto.objects.get(pk=producto_id)
    objProducto = get_object_or_404(Producto,pk=producto_id)
    context = {
        'producto':objProducto
    }

    return render(request, 'web/producto_detalle.html', context)

def todos_los_usuarios ( request ):
    return render( request, 'web/todos_los_usuarios.html' )










