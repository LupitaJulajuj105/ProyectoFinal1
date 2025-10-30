from django.shortcuts import render, redirect, get_object_or_404
from .models import Beca
from .forms import BecaForm

def lista(request):
    becas = Beca.objects.all()
    return render(request, 'becas/lista.html', {'becas': becas})

def crear(request):
    if request.method == 'POST':
        form = BecaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('becas_list')
    else:
        form = BecaForm()
    return render(request, 'becas/form.html', {'form': form, 'titulo': 'Nueva Beca'})

def editar(request, id):
    b = get_object_or_404(Beca, id_beca=id)
    if request.method == 'POST':
        form = BecaForm(request.POST, instance=b)
        if form.is_valid():
            form.save()
            return redirect('becas_list')
    else:
        form = BecaForm(instance=b)
    return render(request, 'becas/form.html', {'form': form, 'titulo': 'Editar Beca'})


def becas_list(request):
    becas = Beca.objects.all()
    return render(request, "becas/lista.html", {"becas": becas})

def becas_detail(request, id):
    beca = get_object_or_404(Beca, id_beca=id)
    return render(request, "becas/detalle.html", {"beca": beca})

def detalles_beca(request):
    becas = Beca.objects.all()
    return render(request, "becas/detalleBeca.html", {"becas": becas})