from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['comercial', 'producto', 'cantidad']
        widgets = {
            'cantidad': forms.NumberInput(attrs={
                'min': 1,
                'step': 1,
                'class': 'form-control'
            }),
        }
