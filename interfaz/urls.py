from django.contrib import admin
from django.urls import path
from interfaz import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('inventario/', views.inventario, name='inventario'),
    
]
