from django import forms
from .models import Socioeconomico

class SocioeconomicoForm(forms.ModelForm):
    class Meta:
        model = Socioeconomico
        fields = [
            'nombre_completo',
            'dpi',
            'edad',
            'telefono',
            'correo',
            'direccion',
            'ocupacion_padre',
            'ingreso_padre',
            'ocupacion_madre',
            'ingreso_madre',
            'num_personas_hogar',
            'motivo_beca'
        ]
