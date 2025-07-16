from django.shortcuts import render
from django.shortcuts import redirect
from .models import OrdenProduccion
from .forms import ProduccionForm
from django.shortcuts import get_object_or_404

# List all production orders
def lista_produccion(request):
    producciones = OrdenProduccion.objects.all()
    return render(request, 'produccion/produccion.html', {'producciones': producciones})

# Add a new production order
def agregar_produccion(request):
    if request.method == 'POST':
        form = ProduccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produccion')
    else:
        form = ProduccionForm()
    return render(request, 'produccion/agregar_produccion.html', {'form': form})

# Edit an existing production order
def editar_produccion(request, produccion_id):
    produccion = get_object_or_404(OrdenProduccion, id=produccion_id)
    if request.method == 'POST':
        form = ProduccionForm(request.POST, instance=produccion)
        if form.is_valid():
            form.save()
            return redirect('produccion')
    else:
        form = ProduccionForm(instance=produccion)
    return render(request, 'produccion/editar_produccion.html', {'form': form})

# Delete a production order
def eliminar_produccion(request, produccion_id):
    produccion = get_object_or_404(OrdenProduccion, id=produccion_id)
    if request.method == 'POST':
        produccion.delete()
        return redirect('produccion')
    return render(request, 'produccion/eliminar_produccion.html', {'produccion': produccion})
