from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_finanzas, name='finanzas'),
    path('agregar/', views.agregar_movimiento, name='agregar_movimiento'),
    path('editar/<int:movimiento_id>/', views.editar_movimiento, name='editar_movimiento'),
    path('eliminar/<int:movimiento_id>/', views.eliminar_movimiento, name='eliminar_movimiento'),
]
