from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventario, name='inventario'),
    path('editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]
