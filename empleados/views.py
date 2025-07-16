from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado


def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/empleados.html', {'empleados': empleados})


def agregar_empleado(request):
    if request.method == 'POST':
        Empleado.objects.create(
            nombre=request.POST.get('nombre'),
            dni=request.POST.get('dni'),
            cargo=request.POST.get('cargo'),
            telefono=request.POST.get('telefono'),
            correo=request.POST.get('correo'),
            fecha_ingreso=request.POST.get('fecha_ingreso'),
            activo=bool(request.POST.get('activo'))
        )
        return redirect('empleados')
    return redirect('empleados')


def editar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)

    if request.method == 'POST':
        empleado.nombre = request.POST.get('nombre')
        empleado.dni = request.POST.get('dni')
        empleado.cargo = request.POST.get('cargo')
        empleado.telefono = request.POST.get('telefono')
        empleado.correo = request.POST.get('correo')
        empleado.fecha_ingreso = request.POST.get('fecha_ingreso')
        empleado.activo = bool(request.POST.get('activo'))
        empleado.save()
        return redirect('empleados')

    return redirect('empleados')


def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    empleado.delete()
    return redirect('empleados')
