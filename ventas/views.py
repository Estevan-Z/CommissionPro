from django.shortcuts import render, redirect
from .models import Venta
from .forms import VentaForm
from django.utils.timezone import localtime

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
            form.save()
            return redirect('lista_ventas') 
    else:
        form = VentaForm()
    return render(request, 'ventas/crear_venta.html', {'form': form})
