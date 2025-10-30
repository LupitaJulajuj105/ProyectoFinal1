from django.shortcuts import render
from django.db.models import Q
from .models import DatosAcademicos, Documento, HistorialBecas, HistorialUsuarios, Estudiante


# 🔹 CONSULTA DE DATOS ACADÉMICOS
def consulta_datos_academicos(request):
    modo = 'grupal'
    resultados = DatosAcademicos.objects.all()

    if request.method == 'POST':
        q = request.POST.get('q', '').strip()
        if q:
            if q.isdigit():
                resultados = DatosAcademicos.objects.filter(estudiante_id=int(q))
                modo = 'individual'
            else:
                estudiantes = Estudiante.objects.filter(
                    Q(nombre__icontains=q) | Q(apellido__icontains=q)
                ).values_list('id', flat=True)
                resultados = DatosAcademicos.objects.filter(estudiante_id__in=estudiantes)
                modo = 'individual'

    return render(request, 'consultas/datosacademicos.html', {'resultados': resultados, 'modo': modo})


# 🔹 CONSULTA DE DOCUMENTOS
def consulta_documentos(request):
    modo = 'grupal'
    resultados = Documento.objects.all()

    if request.method == 'POST':
        q = request.POST.get('q', '').strip()
        if q:
            if q.isdigit():
                resultados = Documento.objects.filter(solicitud__id_solicitud=int(q))
                modo = 'individual'
            else:
                solicitudes = Solicitud.objects.filter(
                    Q(estudiante__nombre__icontains=q) | Q(estudiante__apellido__icontains=q)
                )
                resultados = Documento.objects.filter(solicitud__in=solicitudes)
                modo = 'individual'

    return render(request, 'consultas/documentos.html', {'resultados': resultados, 'modo': modo})


# 🔹 CONSULTA DE HISTORIAL DE BECAS
def consulta_historial_becas(request):
    modo = 'grupal'
    resultados = HistorialBecas.objects.all()

    if request.method == 'POST':
        q = request.POST.get('q', '').strip()
        if q:
            if q.isdigit():
                resultados = HistorialBecas.objects.filter(estudiante_id=int(q))
                modo = 'individual'
            else:
                estudiantes = Estudiante.objects.filter(
                    Q(nombre__icontains=q) | Q(apellido__icontains=q)
                ).values_list('id', flat=True)
                resultados = HistorialBecas.objects.filter(estudiante_id__in=estudiantes)
                modo = 'individual'

    return render(request, 'consultas/historialbecas.html', {'resultados': resultados, 'modo': modo})


# 🔹 CONSULTA DE HISTORIAL DE USUARIOS
def consulta_historial_usuarios(request):
    modo = 'grupal'
    resultados = HistorialUsuarios.objects.all()

    if request.method == 'POST':
        q = request.POST.get('q', '').strip()
        if q and not q.isdigit():
            resultados = HistorialUsuarios.objects.filter(accion__icontains=q)
            modo = 'individual'

    return render(request, 'consultas/historialusuarios.html', {'resultados': resultados, 'modo': modo})
# 🔹 CONSULTA DE DATOS SOCIOECONÓMICOS
from .models import Socioeconomico  # 👈 Asegúrate de importar el modelo arriba del archivo

def consulta_socioeconomicos(request):
    modo = 'grupal'
    resultados = Socioeconomico.objects.all()

    if request.method == 'POST':
        q = request.POST.get('q', '').strip()
        if q:
            if q.isdigit():
                # Buscar por ID de estudiante
                resultados = Socioeconomico.objects.filter(estudiante_id=int(q))
                modo = 'individual'
            else:
                # Buscar por nombre o apellido del estudiante
                estudiantes = Estudiante.objects.filter(
                    Q(nombre__icontains=q) | Q(apellido__icontains=q)
                ).values_list('id', flat=True)
                resultados = Socioeconomico.objects.filter(estudiante_id__in=estudiantes)
                modo = 'individual'

    return render(request, 'consultas/socioeconomicos.html', {'resultados': resultados, 'modo': modo})
