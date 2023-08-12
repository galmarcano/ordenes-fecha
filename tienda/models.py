from django.db import models

# Create your models here.
class Orden(models.Model):
    cliente = models.CharField(max_length = 128)
    direccion = models.CharField(max_length = 256)
    fecha = models.DateField() #año-mes-dia
    fecha_envio = models.DateTimeField() #año-mes-dia hora-min-seg zona horaria

    def __str__(self):
        return self.cliente

class Producto(models.Model):
    nombre = models.CharField(max_length = 128)
    descripcion = models.CharField(max_length = 128)
    precio = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nombre

class Detalle(models.Model):
    orden = models.ForeignKey(Orden, on_delete = models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete = models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio = models.PositiveIntegerField()