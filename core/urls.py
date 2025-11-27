from core.views.mallo import MalloCategoryView, MalloDatosView, MalloSacarDatosView
from django.urls import path

urlpatterns = [
    # Categories
    path("category/", MalloCategoryView.as_view(), name="category-list"),
    path("category/<int:pk>/", MalloCategoryView.as_view(), name="category-detail"),
    
    #Datos
    path("datos/", MalloDatosView.as_view(), name="datos-list"),
    path("datos/<int:pk>/", MalloDatosView.as_view(), name="datos-detail"),

    # Salidas
    path("salida/", MalloSacarDatosView.as_view(), name="salidas-list"),
    path("salida/<int:pk>/", MalloSacarDatosView.as_view(), name="salida-detail")
]