from django.contrib import admin
from .models import Proveedor, Compra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'proveedor', 'fecha', 'total')

admin.site.register(Proveedor)
