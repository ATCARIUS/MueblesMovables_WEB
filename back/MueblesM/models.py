from django.db import models

# Create your models here.

class Descripcion(models.Model):
    descripcion = models.CharField(max_length= 50)

    def __str__(self):
        return self.descripcion

class Auto(models.Model):
    modelo = models.CharField(max_length=50)
    precio= models.IntegerField()
    detalle= models.TextField()
    nueva = models.BooleanField()
    fecha_fabricacion = models.DateField()
    descripcion = models.ForeignKey(Descripcion, on_delete=models.PROTECT)

    def __str__(self):
        return self.modelo
