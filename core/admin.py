from django.contrib import admin
from .models.mallo import MalloCategory, MalloDatos, MalloSacarDatos
from .models.empresa import Empresa, PerfilUsuario
# Register your models here.

# MALLO
admin.site.register(MalloCategory)
admin.site.register(MalloDatos)
admin.site.register(MalloSacarDatos)

# Empresa
admin.site.register(Empresa)
admin.site.register(PerfilUsuario)