from .models import Category, Datos
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class DatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dato
        fiedls = "__all__"
