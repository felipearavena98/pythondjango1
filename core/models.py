from django.db import models
from django.utils import timezone

class Empresa(models.Model):
    rutEmpresa = models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=100)
    razonSocial = models.CharField(max_length=100)
    correo = models.EmailField(max_length=200)
    telefono = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
        return self.razonSocial


class Colaborador(models.Model):
    rut = models.IntegerField(primary_key=True)
    nombreCompleto = models.CharField(max_length=150)
    sexo = models.CharField(max_length=50)
    fechaNacimiento = models.DateField(auto_now=False, auto_now_add=False)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
        return self.nombreCompleto

class Insumo(models.Model):
    idProducto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    stock = models.IntegerField()
    rutEmpresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    objects = models.Manager()

    def __str__(self):
        return self.nombre

def get_default_my_hour():
      hour = timezone.now()
      formatedHour = hour.strftime("%R")
      return formatedHour

class Turno(models.Model):
    latitud = models.CharField(max_length=20)
    longitud = models.CharField(max_length=20)
    fecha = models.DateField()
    hora = models.CharField(max_length=50, default=get_default_my_hour)
    registro = models.CharField(max_length=20)
    rut = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
