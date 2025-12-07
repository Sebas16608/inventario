from core.models.veterinaria import VetCategory, VetDatos, VetEntrada, VetSacarDatos
from rest_framework import serializers

class VetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VetCategory
        fields = "__all__"

class VetDatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = VetDatos
        fields = "__all__"

class VetEntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VetEntrada
        fields = "__all__"

class VetSalidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VetSacarDatos
        fields = "__all__"