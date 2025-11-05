from django.shortcuts import render, redirect, get_object_or_404
from .models import Solicitud
from .forms import SolicitudForm
from django.contrib import messages

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

def detalles_soli(request):
    solicitudes = Solicitud.objects.all()
    return render(request, "solicitudes/SoliDetalle.html", {"solicitudes": solicitudes})

def estado_solicitud(request, id_solicitud):
    solicitud = get_object_or_404(Solicitud, id_solicitud=id_solicitud)
    return render(request, 'solicitudes/solicitud1.html', {'solicitud': solicitud})


def eliminar(request, id):
    solicitud = get_object_or_404(Solicitud, id_solicitud=id)
    if request.method == 'POST':
        solicitud.delete()
        messages.success(request, 'La solicitud ha sido eliminada correctamente.')
        return redirect('solicitudes_list')
    return render(request, 'solicitudes/solicitudes_confirm_delete.html', {'solicitud': solicitud})