from django.shortcuts import render, redirect
from .models import Venta
from .forms import VentaForm
from django.utils.timezone import localtime
from django.http import JsonResponse 
from django.utils import timezone

def lista_ventas(request):
    ventas_por_comercial = {}
    comisiones_totales = {}

    ventas = Venta.objects.select_related('comercial', 'producto').all()

    for venta in ventas:
        comercial = venta.comercial
        producto = venta.producto.nombre

        if comercial not in ventas_por_comercial:
            ventas_por_comercial[comercial] = {}
            comisiones_totales[comercial] = 0  

        if producto not in ventas_por_comercial[comercial]:
            ventas_por_comercial[comercial][producto] = {
                "cantidad": 0,
                "comision_total": 0,
                "fecha": venta.fecha,  
            }

        ventas_por_comercial[comercial][producto]["cantidad"] += venta.cantidad
        ventas_por_comercial[comercial][producto]["comision_total"] += venta.comision_total
        ventas_por_comercial[comercial][producto]["fecha"] = localtime(venta.fecha)

        comisiones_totales[comercial] += venta.comision_total

    return render(request, 'ventas/lista_ventas.html', {
        'ventas_por_comercial': ventas_por_comercial,
        'comisiones_totales': comisiones_totales,
    })

def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'message': 'Venta Registrada exitosamente!',
                    'fecha': venta.fecha.strftime("%d/%m/%Y")  
                })
            return redirect('lista_ventas')
    else:
        initial_data = {'fecha': timezone.now().strftime('%Y-%m-%d')} 
        form = VentaForm(initial=initial_data)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'ventas/crear_venta.html', {'form': form})

    return render(request, 'ventas/crear_venta.html', {'form': form})

from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def editar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    
    if request.method == 'GET':
        form = VentaForm(instance=venta)
        return render(request, 'ventas/editar_venta.html', {
            'form': form,
            'venta_id': id  # Pasar el ID para el formulario
        })
    
    # POST handling
    form = VentaForm(request.POST, instance=venta)
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'Venta actualizada exitosamente!'})
    return JsonResponse({'errors': form.errors}, status=400)

@require_POST
def eliminar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    venta.delete()
    return JsonResponse({'success': True, 'message': 'Venta eliminada correctamente'})


