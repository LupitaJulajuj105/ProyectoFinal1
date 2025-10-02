from django import forms
from .models import Beca
class BecaForm(forms.ModelForm):
    class Meta:
        model = Beca
        fields = ['nombre','descripcion','tipo_beca','monto','promedio_minimo']
