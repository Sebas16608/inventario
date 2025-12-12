from core.views.mallo import MalloCategoryView, MalloDatosView, MalloSacarDatosView, MalloEntradaView
from core.views.veterinaria import VetCategoryView, VetDatosView, VetEntradaView, VetSalidaView
from django.urls import path

urlpatterns = [
    # ==== MALLO ====
    # Categories
    path("mallo-category/", MalloCategoryView.as_view(), name="mallo-category-list"),
    path("mallo-category/<int:pk>/", MalloCategoryView.as_view(), name="mallo-category-detail"),
    
    #Datos
    path("mallo-datos/", MalloDatosView.as_view(), name="mallo-datos-list"),
    path("mallo-datos/<int:pk>/", MalloDatosView.as_view(), name="mallo-datos-detail"),

    # Entradas
    path("mallo-entrada/", MalloEntradaView.as_view(), name="mallo-entradas-list"),
    path("mallo-entrada/<int:pk>/", MalloEntradaView.as_view(), name="mallo-entradas-detail"),

    # Salidas
    path("mallo-salida/", MalloSacarDatosView.as_view(), name="mallo-salidas-list"),
    path("mallo-salida/<int:pk>/", MalloSacarDatosView.as_view(), name="mallo-salida-detail"),

    # ==== VETERINARIA ====
    # categoria
    path("vet-category/", VetCategoryView.as_view(), name="vet-categoria-list"),
    path("vet-category/<int:pk>/", VetCategoryView.as_view(), name="vet-categoty-detail"),

    # Datos
    path("vet-datos/", VetDatosView.as_view(), name="vet-datos-list"),
    path("vet-datos/<int:pk>/", VetDatosView.as_view(), name="vet-datos-detail"),

    # Entradas
    path("vet-entradas/", VetEntradaView.as_view(), name="vet-entrada-list"),
    path("vet-entradas/<int:pk>/", VetEntradaView.as_view(), name="vet-entradas-detail"),

    # Salidas
    path("vet-salidas/", VetSalidaView.as_view(), name="vet-salida-list"),
    path("vet-salidas/<int:pk>/", VetSalidaView.as_view(), name="vet-salida-detail")
]