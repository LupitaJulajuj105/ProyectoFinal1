from django.db import models

class Estudiante(models.Model):
    GENERO_CHOICES = [('M','Masculino'),('F','Femenino'),('Otro','Otro')]
    ESTADO_CHOICES = [('pendiente','Pendiente'),('aprobado','Aprobado'),('rechazado','Rechazado'),('renovacion','Renovación')]

    id_estudiante = models.AutoField(primary_key=True)
    DPI = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES, null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')

    class Meta:
        db_table = 'estudiantes'
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class HistorialUsuarios(models.Model):
    id_historial = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    accion = models.CharField(max_length=200)
    fecha_hora = models.DateTimeField()

    class Meta:
        db_table = 'historialusuarios'
        managed = False  

    def __str__(self):
        return f"Usuario {self.id_usuario} - {self.accion} en {self.fecha_hora}"
