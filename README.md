# Sistema backend de Inventario
## ¿Por qué lo hice?
En realidad fue porque un primo mio necesitaba ser mas organizado en su trabajo y me pidio favor de programarle algo sencillo, pero luego una prima que es veterinaria tambien necesitaba estar mas organizada en su clínica, asi que decidí aplicar una estructura diferente para poder trabajar de forma mas ordenada y escalable por si alguien llegaba a necesitar la ayuda del sistema.

## ¿Qué es el Proyecto?
Es el backend de un sistema de inventario 100% funcional y escalable

## Tecnologías
1. Python 3.14.2 Usare Python 3.14.2 ya que esta ultima version arreglo la velocidad de python y la velocidad del interprete a la hora de iniciar un servidor me ayuda demasiado.
2. Django 6.0 Usare Django 6.0 debido a que tiene una gran mejor en lo que son tareas en segundo plano, a parte que necesitaba un ORM rapido y sencillo de manejar ya que con la actualizacion de Django 6.0 se optimizo el ORM para el procesamiento de datos mas avanzados.
3. Django Rest Framework 3.16.1 Decidí usar DRF 3.16.1 debido a que mejora la compatibilidad con las nuevas versiones de Python en especial la 3.14 que es con la que trabaje, junto con mejoras de compatibilidad con nuevas versiones de Django ademas que consta de nuevas mejoras en lo que es la compatibilidad con campos nulos con UniqueConstraint agregando tambien mejoras en la vadilacion con los serializadores.

## ¿Qué mejoraria con mas tiempo?
Me dedicaria a aprender Redis y el funcionamiento de la caché para tener una app mas rapida y funcional con alto trafico, ademas que agregaria microservicios que se encarguen de otras funciones como auth y el servicio de facturacion.

## Tiempo
Una semana para la primera parte demo para los clientes.
3 dias para programar y mejorar models, permisos y vistas.
2 dias para pruebas.

## ¿Por qué lo hice con esta estructura?
Debido que hacer apps separadas con modelos iguales en lugar de crear

```bash
.
├── core
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models
│   │   ├── empresa.py
│   │   ├── facturacion.py
│   │   ├── __init__.py
│   │   ├── mallo.py
│   │   └── veterinaria.py
│   ├── permissions
│   │   ├── __init__.py
│   │   ├── mallo.py
│   │   └── veterinaria.py
│   ├── serializers
│   │   ├── empresa.py
│   │   ├── __init__.py
│   │   ├── mallo.py
│   │   └── veterinaria.py
│   ├── templates
│   │   └── mallo
│   │       └── factura-mallo.html
│   ├── urls.py
│   └── views
│       ├── API.py
│       ├── __init__.py
│       ├── mallo.py
│       └── veterinaria.py
├── datos
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── inventario
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── README.md
└── requirements.txt
```
 Debido a que es un sistema muy grande y asi me ahorro tener un models.py enorme mientras va pasando el tiempo

# Como pueden observar tengo 2 apps las cuales son Core y Datos, pero ¿para qué son?
**Datos** fue la primera estructura del sistema en donde es una estructura simple y funcional que use mas que todo para demostracion a los clientes.
**Core** es la estructura final, la app principal bien diseñanda con modelos separados y cada modelo con su propio serializador, vistas y endpoints.

### Conclusión
Tome esta desicion ya que para mi es fue algo nuevo y me gusto porque aprendi demasiado ya que con esta estructura:
1. Es mas facil escalar
2. Codigo facil de mantener
3. Cada modulo vive aislado
