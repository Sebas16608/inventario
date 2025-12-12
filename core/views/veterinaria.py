from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models.veterinaria import VetCategory, VetDatos, VetEntrada, VetSacarDatos
from core.views.API import SuperApiView
from core.serializers.veterinaria import VetCategorySerializer, VetDatosSerializer, VetEntradaSerializer, VetSalidaSerializer
from core.permissions.veterinaria import VetPermisosEscritura, EsSuperUser, VetPermisosLectura, VetPermisos

class VetCategoryView(SuperApiView):
    permission_classes = []
    model  = VetCategory
    serializer_class = VetCategorySerializer

class VetDatosView(SuperApiView):
    permission_classes = []
    model = VetDatos
    serializer_class = VetDatosSerializer

class VetEntradaView(SuperApiView):
    permission_classes = []
    model = VetEntrada
    serializer_class = VetEntradaSerializer

class VetSalidaView(SuperApiView):
    permission_classes = []
    model = VetSacarDatos
    serializer_class = VetSalidaSerializer