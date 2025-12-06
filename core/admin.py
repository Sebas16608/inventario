from django.contrib import admin
from .models.mallo import MalloCategory, MalloDatos, MalloSacarDatos, MalloEntrada
from .models.empresa import Empresa, PerfilUsuario
from .models.veterinaria import VetCategory, VetDatos, VetSacarDatos, VetEntrada
# Register your models here.

# MALLO
admin.site.register(MalloCategory)
admin.site.register(MalloDatos)
admin.site.register(MalloSacarDatos)
admin.site.register(MalloEntrada)

# Veterinaria
admin.site.register(VetCategory)
admin.site.register(VetDatos)
admin.site.register(VetSacarDatos)
admin.site.register(VetEntrada)

# Empresa
admin.site.register(Empresa)
admin.site.register(PerfilUsuario)