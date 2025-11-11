from django.db import models
from django.utils import timezone
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
    presentacion = models.CharField(max_length=255)
    fecha_fabricacion = models.DateField()
    fecha_caducidad = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    precio_descuento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = "Dato"
        verbose_name_plural = "Datos"

    def __str__(self):
        return f"De {self.nombre} hay {self.cantidad} unidades"

    def pocacantidad(self):
        if self.cantidad <= 5:
            return f"Se necesita más producto: solo hay {self.cantidad} unidad/es"
        return f"Stock suficiente: hay {self.cantidad} unidades"

    def precio_total(self):
        if not self.precio_descuento:
            return f"Sin descuento aplicado: {self.precio}"
        precio_final = self.precio - self.precio_descuento
        return f"Con descuento aplicado: {precio_final:.2f}"

class SacarDatos(models.Model):
    datos = models.ForeignKey(Datos, on_delete=models.CASCADE, related_name="salidas")
    cantidad_sacada = models.PositiveIntegerField()
    fecha_salida = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = "Salida de Producto"
        verbose_name_plural = "Salidas de Productos"

    def __str__(self):
        return f"Se sacaron {self.cantidad_sacada} de {self.datos.nombre}"

    def actualizar_stock(self):
        if self.cantidad_sacada > self.datos.cantidad:
            return f"No hay suficiente stock de {self.datos.nombre}"
        self.datos.cantidad -= self.cantidad_sacada
        self.datos.save()
        return f"Stock actualizado: ahora hay {self.datos.cantidad} unidades"

    def save(self, *args, **kwargs):
        if self.cantidad_sacada > self.datos.cantidad:
            raise ValueError(f"No hay suficiente stock de {self.datos.nombre}")
        self.datos.cantidad -= self.cantidad_sacada
        self.datos.save()
        super().save(*args, **kwargs)

    def total_salida(self):
        return self.cantidad_sacada * self.datos.precio_final()