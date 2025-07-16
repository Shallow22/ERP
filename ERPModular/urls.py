from django.contrib import admin
from django.urls import path, include
from interfaz import views as interfaz_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', interfaz_views.home, name='home'),
    path('inventario/', include('inventario.urls')),
    path('compras/', include('compras.urls')),  # Asegúrate que esto esté
    path('ventas/', include('ventas.urls')),
    path('produccion/', include('produccion.urls')),
    path('finanzas/', include('finanzas.urls')),
    path('clientes/', include('clientes.urls')),
    path('empleados/', include('empleados.urls')),
]
