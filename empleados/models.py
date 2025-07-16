from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    cargo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    fecha_ingreso = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
