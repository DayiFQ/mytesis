from django.db import models

# Create your models here.

class registar_cliente(models.Model):
    nombre = models.CharField(max_length=125)
    apellidos = models.CharField(max_length=255)
    pasaporte = models.CharField(max_length=255)
    fecha_llegada = models.DateField((""), auto_now=False, auto_now_add=False)
    fecha_salida = models.DateField((""), auto_now=False, auto_now_add=False)
    cantidad_noches = models.IntegerField()
    pais = models.CharField(max_length=255)


    
class registrar_gastos(models.Model):
    descripcion_gasto = models.CharField(max_length=255)
    importe = models.IntegerField(max_length= 10)

def __str__(self) -> str:
        return self.nombre, self.apellidos, self.pasaporte, self.fecha_llegada, self.fecha_salida, self.cantidad_noches, self.cantidad_noches, self.descripcion_gasto

