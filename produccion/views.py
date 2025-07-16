from django.shortcuts import render, redirect, get_object_or_404
from .models import OrdenProduccion

# List all production orders
def lista_produccion(request):
    producciones = OrdenProduccion.objects.all()
    return render(request, 'produccion/produccion.html', {'producciones': producciones})

# Add a new production order
def agregar_produccion(request):
    if request.method == 'POST':
        OrdenProduccion.objects.create(
            producto=request.POST.get('producto'),
            cantidad=request.POST.get('cantidad'),
            fecha_inicio=request.POST.get('fecha_inicio'),
            fecha_fin=request.POST.get('fecha_fin'),
            estado=request.POST.get('estado')
        )
    return redirect('produccion')

# Edit an existing production order
def editar_produccion(request, produccion_id):
    produccion = get_object_or_404(OrdenProduccion, id=produccion_id)
    if request.method == 'POST':
        produccion.producto = request.POST.get('producto')
        produccion.cantidad = request.POST.get('cantidad')
        produccion.fecha_inicio = request.POST.get('fecha_inicio')
        produccion.fecha_fin = request.POST.get('fecha_fin')
        produccion.estado = request.POST.get('estado')
        produccion.save()
    return redirect('produccion')

# Delete a production order
def eliminar_produccion(request, produccion_id):
    produccion = get_object_or_404(OrdenProduccion, id=produccion_id)
    produccion.delete()
    return redirect('produccion')
