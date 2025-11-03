from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante
from .forms import EstudianteForm


# Listado
def lista(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'beneficiarios/lista.html', {'estudiantes': estudiantes})

# Crear
def crear(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beneficiarios_list')
    else:
        form = EstudianteForm()
    return render(request, 'beneficiarios/form.html', {'form': form, 'titulo': 'Nuevo Beneficiario'})

# Editar
def editar(request, id):
    es = get_object_or_404(Estudiante, id_estudiante=id)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=es)
        if form.is_valid():
            form.save()
            return redirect('beneficiarios_list')
    else:
        form = EstudianteForm(instance=es)
    return render(request, 'beneficiarios/form.html', {'form': form, 'titulo': 'Editar Beneficiario'})


def detalle(request, id):
    es = get_object_or_404(Estudiante, id_estudiante=id)
    return render(request, 'beneficiarios/detalle.html', {'estudiante': es})



def buscar_eliminar_beneficiario(request):
    query = request.GET.get("q")
    resultados = None

    if query:
        # Asegúrate de excluir registros sin id_estudiante, por si acaso
        resultados = Estudiante.objects.filter(
            nombre__icontains=query
        ).exclude(id_estudiante__isnull=True)

    return render(
        request,
        "beneficiarios/buscar_eliminar.html",
        {
            "resultados": resultados,
            "query": query
        }
    )

def eliminar_beneficiario(request, id):
    # Buscar por id_estudiante (no por id normal)
    estudiante = get_object_or_404(Estudiante, id_estudiante=id)

    if request.method == "POST":
        estudiante.delete()
        return redirect("beneficiarios_list")  # Asegúrate de que esta URL exista en urls.py

    return render(
        request,
        "beneficiarios/eliminar_confirmacion.html",
        {
            "beneficiario": estudiante  # usamos "beneficiario" para coincidir con el template
        }
    )
def detalles_bene(request):
    beneficiarios = Estudiante.objects.all()  # Trae todos los beneficiarios
    return render(request, "beneficiarios/detalleBene.html", {"beneficiarios": beneficiarios})