from django.db import models

class OrdenProduccion(models.Model):
    producto = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('pendiente', 'Pendiente'),
            ('en_proceso', 'En Proceso'),
            ('finalizado', 'Finalizado')
        ],
        default='pendiente'
    )

    def __str__(self):
        return f"Producción de {self.producto} - {self.cantidad}"