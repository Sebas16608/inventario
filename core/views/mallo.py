from core.models.mallo import MalloCategory, MalloDatos, MalloSacarDatos, MalloEntrada
from core.serializers.mallo import MalloCategorySerializer, MalloDatosSerializer, MalloSacarDatosSerializer, MalloEntradaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.permissions.mallo import MalloPermisos, EsSuperUser, MalloPermisosLectura, MalloPermisosEscritura

def notexist():
    return {"error": "los datos no fueron encontrados"}

class SuperApiView(APIView):
    model = None
    serializer_class =None

    def get(self, request, pk=None):
        if pk:
            try:
                obj = self.model.objects.get(pk=pk)
                serializer = self.serializer_class(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except self.model.DoesNotExist:
                return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        else:
            obj = self.model.objects.all()
            serializer = self.serializer_class(obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            obj = self.model.objects.get(pk = pk)
        except self.model.DoesNotexist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(obj, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            obj = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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