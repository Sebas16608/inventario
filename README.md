# Sistema Backend de Inventario

## Descripción
Backend de un sistema de inventario **modular, escalable y orientado a producción**, diseñado para adaptarse a distintos tipos de negocio (comercial y clínico), manteniendo una base de código organizada y mantenible.

---

## Contexto y motivación
El proyecto nació a partir de una **necesidad real de organización operativa** en un negocio familiar.  
Posteriormente fue adaptado para una clínica veterinaria, lo que impulsó un **rediseño de la arquitectura** para permitir reutilización, escalabilidad y fácil mantenimiento para futuros clientes.

---

## Tecnologías
- **Python 3.13.7**
- **Django 5.2.7**
- **Django Rest Framework 3.16.1**
- **ASGI (asgiref 3.10.0)** — preparado para async
- **WeasyPrint 66.0** — generación de documentos PDF
- **Django Jazzmin 3.0.1** — personalización del panel de administración

> El proyecto inició usando versiones recientes del stack con fines de aprendizaje y validación de la arquitectura.  
> Durante el desarrollo se realizó una **migración y estabilización** hacia versiones compatibles y listas para producción.

---

## Estructura del proyecto
El sistema está organizado en dos aplicaciones principales:

```bash
core/
datos/
```

### App `datos`
- Primera versión funcional del sistema
- Arquitectura simple
- Usada como **demo inicial para clientes**
- Permitió validar flujos y requerimientos

### App `core`
- Arquitectura final del sistema
- Código organizado por dominio
- Modelos desacoplados
- Cada módulo cuenta con:
  - Serializadores propios
  - Vistas y endpoints independientes
  - Permisos específicos

Esta separación evita archivos monolíticos y facilita la **evolución del sistema a largo plazo**.

---

## Decisiones de diseño
- Prioridad en **modularidad y mantenibilidad**
- Separación por dominio en lugar de estructuras monolíticas
- Evitar duplicación de modelos
- Preparado para agregar nuevos módulos sin afectar los existentes

---

## Tiempo de desarrollo
- **1 semana**: versión demo inicial
- **3 días**: refactorización de modelos, permisos y vistas
- **2 días**: pruebas y ajustes

---

## Mejoras futuras
- Implementación de **Redis** para caché y rendimiento
- Separación en **microservicios** (auth, facturación)
- Tests automatizados
- Métricas y monitoreo

---

## Conclusión
Este proyecto me permitió trabajar con **problemas reales de backend**, como:
- Escalabilidad
- Organización de código
- Diseño de APIs mantenibles

La arquitectura resultante facilita:
1. Escalado progresivo  
2. Mantenimiento del código  
3. Aislamiento por dominio  
