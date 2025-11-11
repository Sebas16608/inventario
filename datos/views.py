from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import CategoryMalloSerializer, DatosMalloSerializer, CategoryVetSerializer, DatoVetSerializer
from .models import Category, Datos
# Create your views here.

def notexist():
    return {"error": "Los datos no fueron entontrados"}

"""
API categorias de MALLO
"""

class CategoryMalloView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                category = Category.objects.get(pk=pk)
                serializer = CategoryMalloSerializer(category)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Category.DoesNotExist:
                return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        else:
            category = Category.objects.all()
            serializer = CategoryMalloSerializer(category, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategoryMalloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategoryMalloSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
"""
API datos MALLO
"""
class DatosMalloView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                datos = Datos.objects.get(pk=pk)
                serializer = DatosMalloSerializer(datos)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Datos.DoesNotExist:
                return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        else:
            datos = Datos.objects.all()
            serializer = DatosMalloSerializer(datos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = DatosMalloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            dato = Datos.objects.get(pk=pk)
        except Datos.DoesNotExist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        
        serializer = DatosMalloSerializer(dato, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            dato = Datos.objects.get(pk=pk)
        except Datos.DoesNotExist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        
        dato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
"""
Categoria Veterinaria
"""
class CategoriaVetView(APIView):
    pass