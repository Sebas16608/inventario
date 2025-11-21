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
        else:
            category = MalloCategory.objects.all()
            serializer = MalloCategorySerializer(category, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = MalloCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            category = MalloCategory.objects.get(pk=pk)
        except MalloCategory.DoesNotExist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        
        serilizer = MalloCategorySerializer(category, data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            category = MalloCategory.objects.get(pk=pk)
        except MalloCategory.DoesNotExist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class MalloDatosView(APIView):
    permission_classes = [MalloPermisos]
    def get(self, request, pk=None):
        if pk:
            try:
                dato = MalloDatos.objects.get(pk=pk)
                serializer = MalloDatosSerializer(dato)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except MalloDatos.DoesNotExist:
                return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        else:
            dato = MalloDatos.objects.all()
            serializer = MalloDatosSerializer(dato, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = MalloDatosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
