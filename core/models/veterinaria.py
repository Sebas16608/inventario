from django.db import models
from core.models.empresa import Empresa
from django.utils import timezone

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
    cantidad_sacada = models.PositiveIntegerField()
    fecha_salida = models.DateField(default=timezone.now)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Salida  de Producto"
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

class VetEntrada(models.Model):
    datos = models.ForeignKey(VetDatos, on_delete=models.CASCADE, related_name="entradas")
    cantidad_ingresada = models.PositiveIntegerField()
    fecha_de_ingreso = models.DateField(default=timezone.now)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Ingreso de Producto"
        verbose_name_plural = "Ingresos de Producto"

    def __str__(self):
        return f"Se ingresaron {self.cantidad_ingresada} unidad/es de {self.datos.nombre}"
    
    def save(self, *args, **kwargs):
        # Actualizar stock antes de guardar la entrada
        self.datos.cantidad += self.cantidad_ingresada
        self.datos.save()
        super().save(*args, **kwargs)

    def total_entrada(self):
        return self.cantidad_ingresada