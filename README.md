# 📦 Sistema de Inventario — Backend (Django REST)

Un sistema de inventario modular construido con Django y Django REST Framework, dividido en dos apps principales:
core (lógica empresarial modularizada) y datos (gestión general de datos e inventario).

## 🚀 Características principales

API REST moderna con Django REST Framework

Arquitectura modular por dominio (empresa, veterinaria, mallo)

Serializers, views y permisos independientes por módulo

Escalable para múltiples tipos de negocios

Configuración limpia y mantenible

Organización profesional tipo “large scale Django project”

🗂️ Estructura del proyecto
```bash
inventario/
├── core
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models
│   │   ├── empresa.py
│   │   ├── __init__.py
│   │   ├── mallo.py
│   │   └── veterinaria.py
│   ├── permissions
│   │   ├── __init__.py
│   │   ├── mallo.py
│   │   └── veterinaria.py
│   ├── serializers
│   │   ├── __init__.py
│   │   ├── mallo.py
│   │   └── veterinaria.py
│   ├── urls.py
│   └── views
│       ├── __init__.py
│       ├── mallo.py
│       └── veterinaria.py
├── datos
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── inventario
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── README.md
└── requirements.txt
```
## 🧩 Arquitectura
# 📁 core

Contiene la lógica modularizada:

models/ → modelos separados por área

serializers/ → serializadores para cada módulo

views/ → endpoints independientes

permissions/ → permisos por tipo de negocio

urls.py → ruteo propio del módulo

Ideal para expandir a nuevos tipos de negocios sin romper nada.

## 📁 datos

Maneja:

Datos generales del sistema

Modelos globales

Endpoints CRUD generales

Perfecto para datos que no pertenecen a un área específica.

# 📦 Requerimientos

Incluye archivo:
```bash
requirements.txt
```
Con todas las dependencias necesarias del proyecto.

# 👨‍💻 Autor

Ángel Sebastian Rodas Rodríguez (Sebas)
Desarrollador Web & Backend
Guatemala 🇬🇹
