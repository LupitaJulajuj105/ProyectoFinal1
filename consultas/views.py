from django.shortcuts import render
from .models import DatosAcademicos, Documento, HistorialBecas, HistorialUsuarios, Socioeconomico

def consulta_datos_academicos(request):
    resultados = None
    modo = 'grupal'
    if request.method == 'POST':
        q = request.POST.get('q','').strip()
        if q:
            if q.isdigit():
                resultados = DatosAcademicos.objects.filter(estudiante_id=int(q))
                modo = 'individual'
            else:
                resultados = DatosAcademicos.objects.filter(estudiante__nombre__icontains=q) | DatosAcademicos.objects.filter(estudiante__apellido__icontains=q)
                modo = 'individual'
        else:
            resultados = DatosAcademicos.objects.all()
    else:
        resultados = DatosAcademicos.objects.all()
    return render(request, 'consultas/datosacademicos.html', {'resultados': resultados, 'modo': modo})

def consulta_documentos(request):
    resultados = None
    modo = 'grupal'
    if request.method == 'POST':
        q = request.POST.get('q','').strip()
        if q and q.isdigit():
            resultados = Documento.objects.filter(solicitud__id_solicitud=int(q))
            modo = 'individual'
        else:
            resultados = Documento.objects.all()
    else:
        resultados = Documento.objects.all()
    return render(request, 'consultas/documentos.html', {'resultados': resultados, 'modo': modo})

def consulta_historial_becas(request):
    resultados = None
    modo = 'grupal'
    if request.method == 'POST':
        q = request.POST.get('q','').strip()
        if q:
            if q.isdigit():
                resultados = HistorialBecas.objects.filter(estudiante_id=int(q))
                modo = 'individual'
            else:
                resultados = HistorialBecas.objects.filter(estudiante__nombre__icontains=q) | HistorialBecas.objects.filter(estudiante__apellido__icontains=q)
                modo = 'individual'
        else:
            resultados = HistorialBecas.objects.all()
    else:
        resultados = HistorialBecas.objects.all()
    return render(request, 'consultas/historialbecas.html', {'resultados': resultados, 'modo': modo})

def consulta_historial_usuarios(request):
    resultados = None
    modo = 'grupal'
    if request.method == 'POST':
        q = request.POST.get('q','').strip()
        if q and not q.isdigit():
            resultados = HistorialUsuarios.objects.filter(accion__icontains=q)
            modo = 'individual'
        else:
            resultados = HistorialUsuarios.objects.all()
    else:
        resultados = HistorialUsuarios.objects.all()
    return render(request, 'consultas/historialusuarios.html', {'resultados': resultados, 'modo': modo})

def consulta_socioeconomicos(request):
    resultados = None
    modo = 'grupal'
    if request.method == 'POST':
        q = request.POST.get('q','').strip()
        if q and q.isdigit():
            resultados = Socioeconomico.objects.filter(estudiante_id=int(q))
            modo = 'individual'
        else:
            resultados = Socioeconomico.objects.all()
    else:
        resultados = Socioeconomico.objects.all()
    return render(request, 'consultas/socioeconomicos.html', {'resultados': resultados, 'modo': modo})
