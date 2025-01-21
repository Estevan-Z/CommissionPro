from django.shortcuts import render, redirect
from .models import Venta
from .forms import VentaForm

def lista_ventas(request):
    
    ventas = Venta.objects.all()
    return render(request, 'ventas/lista_ventas.html', {'ventas': ventas})

def crear_venta(request):
    """Vista para crear una nueva venta."""
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas') 
    else:
        form = VentaForm()
    return render(request, 'ventas/crear_venta.html', {'form': form})
