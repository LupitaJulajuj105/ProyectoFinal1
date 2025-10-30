from django.db import models
class Beca(models.Model):
    TIPO_CHOICES = [('academica','Académica'),('cultural','Cultural'),('deportiva','Deportiva'),('economica','Económica')]
    id_beca = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    tipo_beca = models.CharField(max_length=20, choices=TIPO_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    promedio_minimo = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    class Meta:
        db_table = 'becas'
    def __str__(self):
        return self.nombre


class FormularioSocioeconomico(models.Model):
    nombre = models.CharField(max_length=100)
    dpi = models.CharField(max_length=25)
    edad = models.IntegerField(null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    correo = models.EmailField()
    direccion = models.TextField(blank=True)
    ocupacion_padre = models.CharField(max_length=100, blank=True)
    ingreso_padre = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ocupacion_madre = models.CharField(max_length=100, blank=True)
    ingreso_madre = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dependientes = models.IntegerField(null=True, blank=True)
    motivo = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    