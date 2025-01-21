import random
from django.db import models

class Producto(models.Model):
    id = models.CharField(
        max_length=10, 
        primary_key=True, 
        editable=False, 
        unique=True
    )  
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=100, decimal_places=2)
    marca = models.CharField(max_length=100, blank=True, null=True)
    comision = models.DecimalField(max_digits=5, decimal_places=3, help_text="Porcentaje de comisión")

    def save(self, *args, **kwargs):
        if not self.id:  
            while True:
                random_number = random.randint(10000, 99999)  
                new_id = f"Pro-{random_number}"
                if not Producto.objects.filter(id=new_id).exists(): 
                    self.id = new_id
                    break
        super().save(*args, **kwargs)

    def get_precio_en_pesos(self):
        return f"$ {self.precio:,.2f}"  

    def __str__(self):
        return self.nombre
