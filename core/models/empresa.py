from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    creado_en = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nombre
    
#Extender el modelo de User para agregar empresas
User.add_to_class('empresas', models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True, related_name="usuarios"))
