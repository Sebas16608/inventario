from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models.veterinaria import VetCategory, VetDatos, VetEntrada, VetSacarDatos
from core.serializers.veterinaria import VetCategorySerializer, VetDatosSerializer, VetEntradaSerializer, VetSalidaSerializer
from core.permissions.veterinaria import VetPermisosEscritura, EsSuperUser, VetPermisosLectura, VetPermisos

def notexist():
    return {"error": "los datos no fueron encontrados"}

class VetCategoryView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                category = VetCategory.objects.get(pk=pk)
                serializer = VetCategorySerializer(category)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except VetCategory.DoesNotExist:
                return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        else:
            category = VetCategory.objects.all()
            serializer = VetCategorySerializer(category, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = VetCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            category = VetCategory.objects.get(pk=pk)
        except VetCategory.DoesNotExist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        
        serializer = VetCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            category = VetCategory.objects.get(pk=pk)
        except VetCategory.DoesNotExist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VetDatosView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                datos = VetDatos.objects.get(pk=pk)
                serializer = VetDatosSerializer(datos)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except VetDatos.DoesNotExist:
                return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        else:
            datos = VetDatos.objects.all()
            serializer = VetDatosSerializer(datos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = VetDatosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, pk):
        try:
            datos = VetDatos.objects.get(pk=pk)
        except VetDatos.DoesNotExist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        
        serializer = VetDatosSerializer(datos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            datos = VetDatos.objects.get(pk=pk)
        except VetDatos.DoesNotExist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        
        datos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VetEntradaView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                entrada = VetEntrada.objects.get(pk=pk)
                serializer = VetEntradaSerializer(entrada)
                return Response(serializer.dada, status=status.HTTP_200_OK)
            except VetEntrada.DoesNotExist:
                return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        else:
            entrada = VetEntrada.objects.all()
            serializer = VetEntradaSerializer(entrada, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = VetEntradaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
        