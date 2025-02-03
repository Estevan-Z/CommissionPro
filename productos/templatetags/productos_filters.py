from django import template
from decimal import Decimal

register = template.Library()

@register.filter(name='formato_porcentaje')
def formato_porcentaje(valor):
    if isinstance(valor, Decimal) and valor == valor.to_integral_value():  
        return f"{int(valor)}%"  
    else:
        return f"{valor:.1f}%" 