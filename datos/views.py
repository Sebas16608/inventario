from core.views.API import SuperApiView
from .serializers import CategorySerializer, DatosSerializer, SalidaSerializer, EntradaSerializer
from .models import Category, Datos, SacarDatos, Entradas

class CategoryView(SuperApiView):
    model = Category
    serializer_class = CategorySerializer

class DatosView(SuperApiView):
    model = Datos
    serializer_class = DatosSerializer

class SalidaView(SuperApiView):
    model = SacarDatos
    serializer_class = SalidaSerializer

class EntradasView(SuperApiView):
    model = Entradas
    serializer_class = EntradaSerializer

