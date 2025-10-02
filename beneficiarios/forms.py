from django import forms
from .models import Estudiante
class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['DPI','nombre','apellido','fecha_nacimiento','correo','telefono','direccion','genero','estado']
