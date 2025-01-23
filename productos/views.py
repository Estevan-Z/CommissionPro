from django.shortcuts import render, get_object_or_404,  redirect
from .models import Producto
from .forms import ProductosForm
from django.http import JsonResponse

def crear_producto(request):
    if request.method == 'POST':
        form = ProductosForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'message': 'Producto creado exitosamente!'})
            return redirect('lista_productos')
    else:
        form = ProductosForm()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'Productos/crear_producto.html', {'form': form})

    return render(request, 'Productos/crear_producto.html', {'form': form})


def lista_productos(request):
    productos = Producto.objects.all().order_by('nombre')  
    return render(request, 'Productos/lista_productos.html', {'productos': productos})


def eliminar_producto(request, id):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, id=id)
        producto.delete()
        return JsonResponse({'message': 'Producto eliminado exitosamente.'})
    return JsonResponse({'error': 'Método no permitido.'}, status=405)


def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductosForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'message': 'Producto editado exitosamente.'})
            return redirect('lista_productos')
    else:
        form = ProductosForm(instance=producto)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'Editar/editar_producto.html', {'form': form, 'producto': producto})

    return render(request, 'Editar/editar_producto.html', {'form': form, 'producto': producto})





