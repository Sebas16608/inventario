from core.views.mallo import MalloCategoryView, MalloDatosView, MalloSacarDatosView, MalloEntradaView
from django.urls import path

urlpatterns = [
    # Categories
    path("category/", MalloCategoryView.as_view(), name="category-list"),
    path("category/<int:pk>/", MalloCategoryView.as_view(), name="category-detail"),
    
    #Datos
    path("datos/", MalloDatosView.as_view(), name="datos-list"),
    path("datos/<int:pk>/", MalloDatosView.as_view(), name="datos-detail"),

    # Entradas
    path("entrada/", MalloEntradaView.as_view(), name="entradas-list"),
    path("entrada/<int:pk>/", MalloEntradaView.as_view(), name="entradas-detail"),

    # Salidas
    path("salida/", MalloSacarDatosView.as_view(), name="salidas-list"),
    path("salida/<int:pk>/", MalloSacarDatosView.as_view(), name="salida-detail"),
]