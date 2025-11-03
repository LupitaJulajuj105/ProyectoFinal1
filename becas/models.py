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



    