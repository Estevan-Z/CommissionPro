import random
from django.db import models

class Comercial(models.Model):
    id = models.CharField(
        max_length=10, 
        primary_key=True, 
        editable=False, 
        unique=True
    ) 
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    zona = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:  
            while True:
                random_number = random.randint(10000, 99999)  
                new_id = f"Com-{random_number}"
                if not Comercial.objects.filter(id=new_id).exists():
                    self.id = new_id
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre
