from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def lista_clientes(request):
    # Placeholder implementation
    return HttpResponse('Lista de Clientes'.encode())  # Convert content to bytes

def agregar_cliente(request):
    # Placeholder implementation
    return HttpResponse('Agregar Cliente'.encode())  # Convert content to bytes

def editar_cliente(request, cliente_id):
    # Placeholder implementation
    return HttpResponse(f'Editar Cliente {cliente_id}'.encode())  # Convert content to bytes

def eliminar_cliente(request, cliente_id):
    # Placeholder implementation
    return HttpResponse(f'Eliminar Cliente {cliente_id}'.encode())  # Convert content to bytes
