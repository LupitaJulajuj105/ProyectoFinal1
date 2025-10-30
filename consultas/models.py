from django.db import models
from beneficiarios.models import Estudiante
from becas.models import Beca


# 🔹 DATOS ACADÉMICOS
class DatosAcademicos(models.Model):
    id_academico = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, db_column='id_estudiante')
    nivel_academico = models.CharField(max_length=100, null=True, blank=True)
    institucion = models.CharField(max_length=150, null=True, blank=True)
    promedio = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'datosacademicos'
        verbose_name = "Dato Académico"
        verbose_name_plural = "Datos Académicos"

    def __str__(self):
        return f"{self.estudiante} - {self.nivel_academico}"


# 🔹 DOCUMENTOS
class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    solicitud = models.ForeignKey('solicitudes.Solicitud', on_delete=models.CASCADE, db_column='id_solicitud')
    tipo_documento = models.CharField(max_length=100)
    ruta = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'documentos'
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"

    def __str__(self):
        return f"{self.tipo_documento} ({self.solicitud_id})"


# 🔹 HISTORIAL DE BECAS
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
        verbose_name = "Historial de Beca"
        verbose_name_plural = "Historial de Becas"

    def __str__(self):
        return f"{self.estudiante} - {self.beca} ({self.periodo})"


# 🔹 HISTORIAL DE USUARIOS
class HistorialUsuarios(models.Model):
    id_historial = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    accion = models.CharField(max_length=200)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'historialusuarios'
        verbose_name = "Historial de Usuario"
        verbose_name_plural = "Historial de Usuarios"

    def __str__(self):
        return f"Usuario {self.id_usuario} - {self.accion}"


# 🔹 DATOS SOCIOECONÓMICOS (AGREGADO)
class Socioeconomico(models.Model):
    id_socioeconomico = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, db_column='id_estudiante')
    ingreso_familiar = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    personas_dependientes = models.PositiveIntegerField(null=True, blank=True)
    condicion_vivienda = models.CharField(max_length=100, null=True, blank=True)
    tipo_vivienda = models.CharField(max_length=100, null=True, blank=True)
    servicios_basicos = models.CharField(max_length=150, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'socioeconomicos'
        verbose_name = "Dato Socioeconómico"
        verbose_name_plural = "Datos Socioeconómicos"

    def __str__(self):
        return f"{self.estudiante} - {self.ingreso_familiar} Q"

