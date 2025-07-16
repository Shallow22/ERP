from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def lista_finanzas(request):
    # Placeholder implementation
    return HttpResponse(b'Lista de Finanzas')  # Convert content to bytes

def agregar_movimiento(request):
    # Placeholder implementation
    return HttpResponse(b'Agregar Movimiento')  # Convert content to bytes

def editar_movimiento(request, movimiento_id):
    # Placeholder implementation
    return HttpResponse(f'Editar Movimiento {movimiento_id}'.encode())  # Convert content to bytes

def eliminar_movimiento(request, movimiento_id):
    # Placeholder implementation
    return HttpResponse(f'Eliminar Movimiento {movimiento_id}'.encode())  # Convert content to bytes
