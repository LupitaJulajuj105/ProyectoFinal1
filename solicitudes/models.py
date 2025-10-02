from django.db import models
from beneficiarios.models import Estudiante
from becas.models import Beca

class Solicitud(models.Model):
    ESTADOS = [('pendiente','Pendiente'),('aprobada','Aprobada'),('rechazada','Rechazada')]
    id_solicitud = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, db_column='id_estudiante')
    beca = models.ForeignKey(Beca, on_delete=models.CASCADE, db_column='id_beca')
    fecha_solicitud = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    observaciones = models.TextField(null=True, blank=True)
    class Meta:
        db_table = 'solicitudes'
    def __str__(self):
        return f"Solicitud {self.id_solicitud} - {self.estudiante}"
