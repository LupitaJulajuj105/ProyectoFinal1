from django.db import models
from beneficiarios.models import Estudiante
from becas.models import Beca

class DatosAcademicos(models.Model):
    id_academico = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, db_column='id_estudiante')
    nivel_academico = models.CharField(max_length=100, null=True, blank=True)
    institucion = models.CharField(max_length=150, null=True, blank=True)
    promedio = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    class Meta:
        db_table = 'datosacademicos'

class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    solicitud = models.ForeignKey('solicitudes.Solicitud', on_delete=models.CASCADE, db_column='id_solicitud')
    tipo_documento = models.CharField(max_length=100)
    ruta = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        db_table = 'documentos'

class HistorialBecas(models.Model):
    id_historial = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, db_column='id_estudiante')
    beca = models.ForeignKey(Beca, on_delete=models.CASCADE, db_column='id_beca')
    periodo = models.CharField(max_length=50, null=True, blank=True)
    promedio_periodo = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, default='vigente')
    class Meta:
        db_table = 'historialbecas'

class HistorialUsuarios(models.Model):
    id_historial = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    accion = models.CharField(max_length=200)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'historialusuarios'

class Socioeconomico(models.Model):
    id_socio = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, db_column='id_estudiante')
    ingreso_familiar = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    situacion = models.CharField(max_length=10, null=True, blank=True)
    class Meta:
        db_table = 'socioeconomicos'
