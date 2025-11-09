from .models import Category, Datos
from rest_framework import serializers

"""MALLO"""
class CategoryMalloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class DatosMalloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datos
        fiedls = "__all__"

"""Veterinaria"""
class CategoryVetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "nombre", "presentacion"]

class DatoVetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datos
        fields = ["id", "nombre", "categoria", "cantidad", "presentacion", "fecha_caducidad", "precio"]

