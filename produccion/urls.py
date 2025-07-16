from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produccion, name='produccion'),
    path('agregar/', views.agregar_produccion, name='agregar_produccion'),
    path('editar/<int:produccion_id>/', views.editar_produccion, name='editar_produccion'),
    path('eliminar/<int:produccion_id>/', views.eliminar_produccion, name='eliminar_produccion'),
]
