from shutil import register_unpack_format
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Datos, SacarDatos, Entradas
from .serializers import CategorySerializer, DatosSerializer, EntradaSerializer, SalidaSerializer

def notexist({"Error": "Los datos no fueron encontrados"})

class CategoryView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                category = Category.objects.get(pk=pk)
                serializer = CategorySerializer(category)
                return Response(serializers.data, status=status.HTTP_200_OK)
            except Category.DoesNotExist:
                return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        else:
            category = Category.objects.all()
            serializer = CategorySerializer(category, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    

