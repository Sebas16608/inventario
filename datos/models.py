from django.db import models

# Create your models here.
class Category(models.Model):
    nombre = models.CharField(max_lenght=255)
    molecula = models.CharField(max_lenght=255)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

class Dato(models.Model):
    categoria = models.ForeInKey(Category, on_delete=models.PROTECT, related_name="dato")
    nombre = modesl.CharField(max_lenght=255)
    introduccion = models.Charfield(max_lenght=255)
    slug = models.SlugField(max_lenght=255, unique=True)
    descripcion = models.TextField()
    cantidad = models.IntegredField()
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    descuento = models.FloatField()

