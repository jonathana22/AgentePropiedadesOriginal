from django.db import models


# Create your models here.



class Propiedad(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=15)
    operacion = models.CharField(max_length=15)
    superficie = models.IntegerField()
    habitaciones = models.IntegerField()
    banno = models.IntegerField()
    ubicacion = models.TextField()
    precio = models.IntegerField()
    descripcion = models.TextField()
    imgane = models.ImageField(upload_to="propiedades", null=True)

    def __str__(self):
        return self.nombre



class Galeria(models.Model):
    propiedad = models.ForeignKey(Propiedad, default=None, on_delete=models.CASCADE)
    foto_galeria = models.FileField(upload_to="Propiedades", null=True )

    def __str__(self):
        return self.propiedad.nombre




class Cliente(models.Model):
    rut = models.CharField(max_length=12)
    nombreCliente = models.CharField(max_length=10)
    primerApellido = models.CharField(max_length=20)
    segundoApellido = models.CharField(max_length=20)
    fecNac = models.DateTimeField
    direccion = models.TextField(max_length=100)

