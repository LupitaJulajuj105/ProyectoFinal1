from django.urls import path
from . import views

urlpatterns = [
    path('datos-academicos/', views.consulta_datos_academicos, name='consulta_datos_academicos'),
    path('documentos/', views.consulta_documentos, name='consulta_documentos'),
    path('historial-becas/', views.consulta_historial_becas, name='consulta_historial_becas'),
    path('historial-usuarios/', views.consulta_historial_usuarios, name='consulta_historial_usuarios'),
    path('socioeconomicos/', views.consulta_socioeconomicos, name='consulta_socioeconomicos'),  # 👈 ESTA LÍNEA ES CLAVE
]

