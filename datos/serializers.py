from .models import Category, Datos, SacarDatos, Entradas
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class DatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datos
        fields = "__all__"

class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entradas
        fields = "__all__"

class SalidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SacarDatos
        fields = "__all__"

