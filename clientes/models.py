from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    fecha_afiliacion = models.DateField()
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    notas = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - {self.empresa}"
