from models.mallo import MalloCategory, MalloDatos, MalloSacarDatos
from serializers.mallo import MalloCategorySerializer, MalloDatosSerializer, MalloSacarDatosSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from permissions.mallo import MalloPermisos

def notexist():
    return {"error": "los datos no fueron encontrados"}

class MalloCategoryView(APIView):
    permission_classes = [MalloPermisos]
    def get(self, request, pk=None):
        if pk:
            try:
                category = MalloCategory.objects.get(pk=pk)
                serializer = MalloCategorySerializer(category)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except MalloCategory.DoesNotExist:
                return Response(notexist(), status=status.HTTP_404_NOT_FOUND)