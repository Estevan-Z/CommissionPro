from django import forms
from .models import Comercial

class ComercialForm(forms.ModelForm):
    class Meta:
        model = Comercial
        fields = ['nombre', 'email', 'telefono', 'zona']
