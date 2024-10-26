from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
    

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.RESTRICT)  
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    descripcion = models.TextField(null = True)
    precio_venta = models.IntegerField()
    precio_compra = models.IntegerField()
    stock = models.IntegerField()
    codigo = models.IntegerField(null = True)
    imagen = models.ImageField(upload_to='productos',blank=True)

    def __str__(self):
        return self.nombre