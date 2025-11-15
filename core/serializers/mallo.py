from models.mallo import MalloCategory, MalloDatos, MalloSacarDatos
from rest_framework import serializers

class MalloCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MalloCategory
        fields = "__all__"

class MalloDatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = MalloDatos
        fields = "__all__"

class MalloSacarDatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = MalloSacarDatos
        fields = "__all__"