from django.db import models

class Category(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre

class Datos(models.Model):
    categoria = models.ForeingKey(Category, on_delete=models.PROTECT, related_name="datos")
    nombre = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    presentacion = models.CharField(max_length=255)
    fecha_fabricacion = models.DateField()
    fecha_caducidad = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)


