from django.shortcuts import render, redirect, get_object_or_404
from .models import Venta

# List all sales
def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/ventas.html', {'ventas': ventas})

# Add a new sale
def agregar_venta(request):
    if request.method == 'POST':
        Venta.objects.create(
            cliente=request.POST.get('cliente'),
            total=request.POST.get('total')
        )
    return redirect('ventas')

# Edit an existing sale
def editar_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    if request.method == 'POST':
        venta.cliente = request.POST.get('cliente')
        venta.total = request.POST.get('total')
        venta.save()
    return redirect('ventas')

# Delete a sale
def eliminar_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    venta.delete()
    return redirect('ventas')
