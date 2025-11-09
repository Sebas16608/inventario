from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategoryMalloSerializer, DatosMalloSerializer, CategoryVetSerializer, DatoVetSerializer
from .models import Category, Datos
# Create your views here.

def notexist():
    return {"error": "Los datos no fueron entontrados"}

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
    