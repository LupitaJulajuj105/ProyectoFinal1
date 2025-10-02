from django.shortcuts import render, redirect, get_object_or_404
from .models import Solicitud
from .forms import SolicitudForm

def lista(request):
    solicitudes = Solicitud.objects.select_related('estudiante','beca').all()
    return render(request, 'solicitudes/lista.html', {'solicitudes': solicitudes})

def crear(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('solicitudes_list')
    else:
        form = SolicitudForm()
    return render(request, 'solicitudes/form.html', {'form': form, 'titulo': 'Nueva Solicitud'})

def editar(request, id):
    s = get_object_or_404(Solicitud, id_solicitud=id)
    if request.method == 'POST':
        form = SolicitudForm(request.POST, instance=s)
        if form.is_valid():
            form.save()
            return redirect('solicitudes_list')
    else:
        form = SolicitudForm(instance=s)
    return render(request, 'solicitudes/form.html', {'form': form, 'titulo': 'Editar Solicitud'})


def solicitudes_list(request):
    solicitudes = Solicitud.objects.all()
    return render(request, "solicitudes/lista.html", {"solicitudes": solicitudes})

def solicitudes_detail(request, id):
    solicitud = get_object_or_404(Solicitud, id_solicitud=id)
    return render(request, "solicitudes/detalle.html", {"solicitud": solicitud})
