from django.db import models

class MovimientoFinanciero(models.Model):
    tipo = models.CharField(
        max_length=10,
        choices=[('ingreso', 'Ingreso'), ('egreso', 'Egreso')]
    )
    descripcion = models.TextField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.tipo} - {self.monto}"
