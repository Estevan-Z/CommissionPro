from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    fecha = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )
    )
    
    class Meta:
        model = Venta
        fields = ['fecha', 'comercial', 'producto', 'cantidad']
        widgets = {
            'cantidad': forms.NumberInput(attrs={
                'min': 1,
                'step': 1,
                'class': 'form-control'
            }),
        }