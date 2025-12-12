from core.models.mallo import MalloCategory, MalloDatos, MalloSacarDatos, MalloEntrada
from core.serializers.mallo import MalloCategorySerializer, MalloDatosSerializer, MalloSacarDatosSerializer, MalloEntradaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.permissions.mallo import MalloPermisos, EsSuperUser, MalloPermisosLectura, MalloPermisosEscritura
from core.views.API import SuperApiView

class MalloCategoryView(SuperApiView):
    permission_classes = []
    model = MalloCategory
    serializer_class = MalloCategorySerializer

class MalloDatosView(SuperApiView):
    permission_classes = []
    model = MalloDatos
    serializer_class = MalloDatosSerializer

class MalloSacarDatosView(SuperApiView):
    permission_classes = []
    model = MalloSacarDatos
    serializer_class = MalloSacarDatosSerializer

class MalloEntradaView(SuperApiView):
    permission_classes = []
    model = MalloEntrada
    serializer_class = MalloEntradaSerializer