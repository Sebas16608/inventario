from django.db import models
from core.models.empresa import Empresa

class VetCategory(models.Model):
    nombre = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, related_name="categorias")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre

class VetDatos(models.Model):
    categoria = models.ForeignKey(VetCategory, on_delete=models.PROTECT, related_name="datos")
    nombre = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    presentacion = models.CharField(max_length=255)
    fecha_caducidad = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Dato Veterinario"
        verbose_name_plural = "Datos Veterinarios"

    def __str__(self):
        return self.nombre
    
class VetSacarDatos(models.Model):
    datos = models.ForeignKey(VetDatos, on_delete=models.PROTECT, related_name="salidas")
    cantidad_sacada = None