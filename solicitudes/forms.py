from django import forms
from .models import Solicitud
class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['estudiante','beca','fecha_solicitud','estado','observaciones']
