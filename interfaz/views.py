from django.shortcuts import render
from inventario.models import Producto

def home(request):
    return render(request, 'interfaz/home.html')

def inventario(request):
    productos = Producto.objects.all()
    return render(request, 'interfaz/inventario.html', {'productos': productos})
