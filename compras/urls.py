from django.urls import path
from . import views

urlpatterns = [
    path('', views.compras, name='compras'),
    path('nueva/', views.nueva_compra, name='nueva_compra'),
    path('editar/<int:compra_id>/', views.editar_compra, name='editar_compra'),
    path('eliminar/<int:compra_id>/', views.eliminar_compra, name='eliminar_compra'),
]
