from django.shortcuts import render
from .models import Comercial

from django.shortcuts import render, redirect
from .forms import ComercialForm

def crear_comercial(request):
    if request.method == 'POST':
        form = ComercialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_comerciales')
    else:
        form = ComercialForm()
    return render(request, 'Comerciales/crear_comercial.html', {'form': form})


def lista_comerciales(request):
    comerciales = Comercial.objects.all()
    return render(request, 'Comerciales/lista_comerciales.html', {'comerciales': comerciales})
