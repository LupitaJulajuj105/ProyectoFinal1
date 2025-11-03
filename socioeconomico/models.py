from django.db import models

class Socioeconomico(models.Model):
    nombre_completo = models.CharField(max_length=255)
    dpi = models.CharField(max_length=20)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    direccion = models.TextField()
    ocupacion_padre = models.CharField(max_length=255)
    ingreso_padre = models.DecimalField(max_digits=10, decimal_places=2)
    ocupacion_madre = models.CharField(max_length=255)
    ingreso_madre = models.DecimalField(max_digits=10, decimal_places=2)
    num_personas_hogar = models.IntegerField()
    motivo_beca = models.TextField()

    def __str__(self):
        return self.nombre_completo


# Create your models here.
