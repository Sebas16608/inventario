from django.db import models

# Agregar categoria
# restar o sumar cada que se agrega o se retira producto
# Costo de producto grande en pocas cantidades ejemplo Litros a ML
# Create your models here.
class Category(models.Model):
    nombre = models.CharField(max_length=255)
    moleculas = models.CharField(max_length=255, blank=True, null=True)
    especie = models.CharField(max_length=255, blank=True, null=True)
    etapa = models.CharField(max_length=255, blank=True, null=True)
    presentacion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre


class Datos(models.Model):
    categoria = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="datos")
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    presentacion = models.CharField(max_length=255, blank=False, null=False)
    fecha_fabricacion = models.DateField()
    fecha_caducidad = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    precio_descuento = models.FloatField(blank=True, null=True)
 
    class Meta:
        verbose_name = "Dato"
        verbose_name_plural = "Datos"

    def __str__(self):
        return f"De {self.nombre} hay {self.cantidad} unidades"

    def pocacantidad(self):
        if self.cantidad <= 5:
            return f"Se necesita mas producto solo hay {self.cantidad} unidad/es"
        return f"Stock suficiente hay {self.cantidad} unidades"
   
    def precio_total(self):
        if self.precio_descuento is None:
            return f"Sin descuento aplicado: {self.precio}"
    
        precio_final = self.precio + self.precio_descuento
        return f"Con descuento aplicado: {precio_final:.2f}"
  
