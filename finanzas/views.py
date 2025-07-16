from django.shortcuts import render, redirect, get_object_or_404
from .models import MovimientoFinanciero


def lista_finanzas(request):
    movimientos = MovimientoFinanciero.objects.all()
    return render(request, 'finanzas/finanzas.html', {'movimientos': movimientos})


def agregar_movimiento(request):
    if request.method == 'POST':
        MovimientoFinanciero.objects.create(
            tipo=request.POST.get('tipo'),
            descripcion=request.POST.get('descripcion'),
            monto=request.POST.get('monto'),
            fecha=request.POST.get('fecha')
        )
    return redirect('finanzas')


def editar_movimiento(request, movimiento_id):
    movimiento = get_object_or_404(MovimientoFinanciero, id=movimiento_id)
    if request.method == 'POST':
        movimiento.tipo = request.POST.get('tipo')
        movimiento.descripcion = request.POST.get('descripcion')
        movimiento.monto = request.POST.get('monto')
        movimiento.fecha = request.POST.get('fecha')
        movimiento.save()
    return redirect('finanzas')


def eliminar_movimiento(request, movimiento_id):
    movimiento = get_object_or_404(MovimientoFinanciero, id=movimiento_id)
    movimiento.delete()
    return redirect('finanzas')
