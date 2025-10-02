from django.urls import path
from . import views
urlpatterns = [
    path('datosacademicos/', views.consulta_datos_academicos, name='consulta_datos_academicos'),
    path('documentos/', views.consulta_documentos, name='consulta_documentos'),
    path('historialbecas/', views.consulta_historial_becas, name='consulta_historial_becas'),
    path('historialusuarios/', views.consulta_historial_usuarios, name='consulta_historial_usuarios'),
    path('socioeconomicos/', views.consulta_socioeconomicos, name='consulta_socioeconomicos'),
]
