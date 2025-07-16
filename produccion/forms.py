from django import forms
from .models import OrdenProduccion

class ProduccionForm(forms.ModelForm):
    class Meta:
        model = OrdenProduccion
        fields = ['producto', 'cantidad', 'fecha_inicio', 'fecha_fin', 'estado'] 