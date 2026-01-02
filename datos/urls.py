from .views import CategoryView, DatosView, SalidaView, EntradasView
from django.urls import path

urlpatterns = [
    path("categoy/", CategoryView.as_view(), name="category-list"),
    path("category/<int:pk>/", CategoryView.as_view(), name="category-detail"),
    path("datos/", DatosView.as_view(), name="datos-list"),
    path("datos/<int:pk>/", DatosView.as_view(), name="datos-detail"),
    path("salida/", SalidaView.as_view(), name="salida-list"),
    path("salida/<int:pk>/", SalidaView.as_view(), name="salida-detail"),
    path("entrada/", EntradasView.as_view(), name="entrada-list"),
    path("entrada/<int:pk>/", EntradasView.as_view(), name="entrada-detail")
]
