from django.contrib import admin
from .models import Category, Datos, SacarDatos
# Register your models here.
@admin.register(Datos)
class DatosAdmin(admin.ModelAdmin):
    list_display = ["nombre", "cantidad", "categoria", "presentacion", "pocacantidad", "precio", "precio_descuento", "precio_total"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["nombre", "moleculas", "especie", "etapa", "presentacion"]

@admin.register(SacarDatos)
class SacarDatosAdmin(admin.ModelAdmin):
    list_display = ["datos", "cantidad_sacada", "fecha_salida"]