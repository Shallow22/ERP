from django.shortcuts import render, redirect, get_object_or_404
from .models import Compra
from .forms import CompraForm

def compras(request):
    compras = Compra.objects.all()
    return render(request, 'compras/compras.html', {'compras': compras})

def nueva_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compras')
    else:
        form = CompraForm()
    return render(request, 'compras/nueva_compra.html', {'form': form})

# Vista para editar una compra
def editar_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    if request.method == 'POST':
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            return redirect('compras')
    else:
        form = CompraForm(instance=compra)
    return render(request, 'compras/editar_compra.html', {'form': form})

# Vista para eliminar una compra
def eliminar_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    if request.method == 'POST':
        compra.delete()
        return redirect('compras')
    return render(request, 'compras/eliminar_compra.html', {'compra': compra})
