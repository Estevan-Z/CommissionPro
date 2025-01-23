from django.shortcuts import render, get_object_or_404,  redirect
from .models import Comercial
from .forms import ComercialForm
from django.http import JsonResponse

def crear_comercial(request):
    if request.method == 'POST':
        form = ComercialForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'message': 'Comercial creado exitosamente!'})
            return redirect('lista_comerciales')
    else:
        form = ComercialForm()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'Comerciales/crear_comercial.html', {'form': form})
    
    return render(request, 'Comerciales/crear_comercial.html', {'form': form})


def lista_comerciales(request):
    comerciales = Comercial.objects.all().order_by('nombre')
    return render(request, 'Comerciales/lista_comerciales.html', {'comerciales': comerciales})


def eliminar_comercial(request, id):
    if request.method == 'POST':
        comercial = get_object_or_404(Comercial, id=id)
        comercial.delete()
        return JsonResponse({'message': 'Producto eliminado exitosamente.'})
    return JsonResponse({'error': 'Método no permitido.'}, status=405)


def editar_comercial(request, id):
    comercial = get_object_or_404(Comercial, id=id)
    if request.method == 'POST':
        form = ComercialForm(request.POST, instance=comercial)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'message': 'Producto editado exitosamente.'})
            return redirect('lista_productos')
    else:
        form = ComercialForm(instance=comercial)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'Editar/Editar_Comercial.html', {'form': form, 'comercial': comercial})

    return render(request, 'Editar/Editar_Comercial.html', {'form': form, 'comercial': comercial})

