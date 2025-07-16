from django.shortcuts import render
from django.db.models import Sum

from inventario.models import Producto
from compras.models import Compra
from ventas.models import Venta
from produccion.models import OrdenProduccion
from finanzas.models import MovimientoFinanciero
from clientes.models import Cliente
from empleados.models import Empleado

def home(request):
    context = {
        'total_productos': Producto.objects.count(),
        'total_compras': Compra.objects.count(),
        'total_ventas': Venta.objects.count(),
        'producciones_pendientes': OrdenProduccion.objects.filter(estado='pendiente').count(),
        'balance_financiero': MovimientoFinanciero.objects.filter(tipo='ingreso').aggregate(total=Sum('monto'))['total'] or 0 -
                             (MovimientoFinanciero.objects.filter(tipo='egreso').aggregate(total=Sum('monto'))['total'] or 0),
        'total_clientes': Cliente.objects.count(),
        'total_empleados': Empleado.objects.count(),
    }
    return render(request, 'interfaz/home.html', context)

def inventario(request):
    productos = Producto.objects.all()
    return render(request, 'interfaz/inventario.html', {'productos': productos})
