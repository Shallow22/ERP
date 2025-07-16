from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_empleados, name='empleados'),
    path('agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('editar/<int:empleado_id>/', views.editar_empleado, name='editar_empleado'),
    path('eliminar/<int:empleado_id>/', views.eliminar_empleado, name='eliminar_empleado'),
]
