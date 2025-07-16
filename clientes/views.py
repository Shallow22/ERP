from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente


def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/clientes.html', {'clientes': clientes})


def agregar_cliente(request):
    if request.method == 'POST':
        Cliente.objects.create(
            nombre=request.POST.get('nombre'),
            empresa=request.POST.get('empresa'),
            fecha_afiliacion=request.POST.get('fecha_afiliacion'),
            correo=request.POST.get('correo'),
            telefono=request.POST.get('telefono'),
            notas=request.POST.get('notas'),
            activo=request.POST.get('activo') == 'True'
        )
    return redirect('clientes')


def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.empresa = request.POST.get('empresa')
        cliente.fecha_afiliacion = request.POST.get('fecha_afiliacion')
        cliente.correo = request.POST.get('correo')
        cliente.telefono = request.POST.get('telefono')
        cliente.notas = request.POST.get('notas')
        cliente.activo = request.POST.get('activo') == 'True'
        cliente.save()
    return redirect('clientes')


def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.delete()
    return redirect('clientes')
