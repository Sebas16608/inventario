from django.contrib import admin
from models.mallo.py import MalloCategory, MalloDatos, MalloSacarDatos
from models.empresa.py import Empresa, PerfilUsuario
# Register your models here.

# MALLO
admin.site.register(MalloCategory)
admin.site.register(MalloDatos)
admin.site.register(MalloSacarDatos)

# Empresa
