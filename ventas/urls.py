from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ventas, name='ventas'),
    path('agregar/', views.agregar_venta, name='agregar_venta'),
    path('editar/<int:venta_id>/', views.editar_venta, name='editar_venta'),
    path('eliminar/<int:venta_id>/', views.eliminar_venta, name='eliminar_venta'),
]
