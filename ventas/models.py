from django.db import models
from comerciales.models import Comercial
from productos.models import Producto

class Venta(models.Model):
    comercial = models.ForeignKey(Comercial, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    cantidad = models.PositiveIntegerField()
    comision_total = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.comision_total = (self.cantidad * self.producto.precio) * (self.producto.comision / 100)
        super().save(*args, **kwargs)

    def comision_total_en_pesos(self):
        return f"${self.comision_total:,f}"

    def __str__(self):
        return f"Venta de {self.cantidad} {self.producto.nombre} por {self.comercial.nombre}"
