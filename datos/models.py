from django.db import models

# Create your models here.
class Category(models.Model):
    nombre = models.CharField(max_lenght=255)
    molecula = models.CharField(max_lenght=255)

class Dato(models.Model):
    nombre = modesl.CharField(max_lenght=255)
    introduccion = models.Charfield(max_lenght=255)
    slug = models.SlugField(max_lenght=255, unique=True)
    descripcion = models.TextField()
    cantidad = models.IntegredField()
    precio = models.DecimalField(º
