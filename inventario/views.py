from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from decimal import Decimal, InvalidOperation
from .models import Producto

# Vista principal: Listar productos y agregar
def inventario(request):
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            categoria = request.POST.get('categoria')
            stock = int(request.POST.get('stock', 0))
            precio = Decimal(request.POST.get('precio', 0))

            Producto.objects.create(
                nombre=nombre,
                categoria=categoria,
                stock=stock,
                precio=precio
            )
            return redirect('inventario')
        except (ValueError, InvalidOperation):
            # Si hay error de conversión, mostrar mensaje de error
            productos = Producto.objects.all()
            return render(request, 'inventario/inventario.html', {
                'productos': productos,
                'error': 'Por favor, ingrese valores válidos para stock y precio'
            })

    productos = Producto.objects.all()
    return render(request, 'inventario/inventario.html', {'productos': productos})

# Vista para editar producto (directamente desde la tabla)
def editar_producto(request, producto_id):
    if request.method == 'POST':
        try:
            producto = get_object_or_404(Producto, id=producto_id)
            producto.nombre = request.POST.get('nombre')
            producto.categoria = request.POST.get('categoria')
            producto.stock = int(request.POST.get('stock', 0))
            producto.precio = Decimal(request.POST.get('precio', 0))
            producto.save()
        except (ValueError, InvalidOperation):
            # Si hay error de conversión, ignorar la actualización
            pass
    return redirect('inventario')

# Vista para eliminar producto (directo sin confirmación)
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('inventario')
