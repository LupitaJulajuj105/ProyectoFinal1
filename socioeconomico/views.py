
from django.shortcuts import render, redirect, get_object_or_404
from .models import Socioeconomico
from .forms import SocioeconomicoForm

# Lista todos los registros
def lista(request):
    registros = Socioeconomico.objects.all()
    return render(request, 'socioeconomico/lista.html', {'socioeconomicos': registros})

# Crear un nuevo registro
def crear(request):
    if request.method == 'POST':
        form = SocioeconomicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('socioeconomico_list')
    else:
        form = SocioeconomicoForm()
    return render(request, 'socioeconomico/form.html', {'form': form, 'titulo': 'Nuevo Registro Socioeconómico'})

# Editar un registro existente
def editar(request, id):
    registro = get_object_or_404(Socioeconomico, id=id)
    if request.method == 'POST':
        form = SocioeconomicoForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('socioeconomico_list')
    else:
        form = SocioeconomicoForm(instance=registro)
    return render(request, 'socioeconomico/form.html', {'form': form, 'titulo': 'Editar Registro Socioeconómico'})

# Ver detalle de un registro
def detalle(request, id):
    registro = get_object_or_404(Socioeconomico, id=id)
    return render(request, 'socioeconomico/detalle.html', {'socioeconomico': registro})

# Eliminar un registro
def eliminar(request, id):
    registro = get_object_or_404(Socioeconomico, id=id)
    if request.method == 'POST':
        registro.delete()
        return redirect('socioeconomico_list')
    return render(request, 'socioeconomico/eliminar.html', {'socioeconomico': registro})

def detalles_socioeconomico(request):
    socioeconomicos = Socioeconomico.objects.all()
    return render(request, "socioeconomico/detalleSocio.html", {"socioeconomicos": socioeconomicos})