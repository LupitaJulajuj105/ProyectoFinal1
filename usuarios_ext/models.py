from django.db import models

class Historial(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    accion = models.CharField(max_length=255)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    tabla = models.CharField(max_length=255)

    class Meta:
        db_table = 'usuarios_ext_historial'  # 👈 Nombre exacto de tu tabla en la BD

