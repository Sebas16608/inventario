from rest_framework import permissions

class MalloPermisos(permissions.BasePermission):
    """
    Permisos para APIs de Mallo - Aislamiento por empresa
    Verifica que el usuario tenga perfil y empresa asignada
    """
    
    def has_permission(self, request, view):
        """
        Verifica permisos a nivel de vista (GET, POST, PUT, DELETE, etc.)
        """
        # Verificar que el usuario esté autenticado, tenga perfil y empresa
        usuario_autenticado = request.user and request.user.is_authenticated
        tiene_perfil = hasattr(request.user, 'perfil')
        tiene_empresa = tiene_perfil and request.user.perfil.empresa is not None
        
        return bool(usuario_autenticado and tiene_perfil and tiene_empresa)
    
    def has_object_permission(self, request, view, obj):
        """
        Verifica permisos a nivel de objeto específico
        Solo permite acceso si el objeto pertenece a la misma empresa del usuario
        """
        # Si el objeto tiene campo 'empresa', verificar que coincida
        if hasattr(obj, 'empresa'):
            return obj.empresa == request.user.perfil.empresa
        
        # Si el objeto no tiene empresa, buscar en relaciones comunes
        elif hasattr(obj, 'usuario') and hasattr(obj.usuario, 'perfil'):
            return obj.usuario.perfil.empresa == request.user.perfil.empresa
        
        elif hasattr(obj, 'categoria') and hasattr(obj.categoria, 'empresa'):
            return obj.categoria.empresa == request.user.perfil.empresa
        
        # Si no se puede determinar la empresa, denegar acceso por seguridad
        return False

class EsSuperUser(permissions.BasePermission):
    """
    Permiso para superusuarios - acceso total sin restricciones de empresa
    """
    
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
    
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_superuser

class MalloPermisosLectura(permissions.BasePermission):
    """
    Permisos solo de lectura para Mallo
    Permite GET sin verificar empresa, pero POST/PUT/DELETE sí requieren empresa
    """
    
    def has_permission(self, request, view):
        # Para métodos de solo lectura (GET, HEAD, OPTIONS), permitir sin empresa
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        
        # Para métodos de escritura, verificar empresa
        usuario_autenticado = request.user and request.user.is_authenticated
        tiene_perfil = hasattr(request.user, 'perfil')
        tiene_empresa = tiene_perfil and request.user.perfil.empresa is not None
        
        return bool(usuario_autenticado and tiene_perfil and tiene_empresa)
    
    def has_object_permission(self, request, view, obj):
        # Para lectura, permitir siempre
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Para escritura, verificar empresa
        if hasattr(obj, 'empresa'):
            return obj.empresa == request.user.perfil.empresa
        
        return False

class MalloPermisosEscritura(permissions.BasePermission):
    """
    Permisos de escritura para Mallo
    Solo permite POST, PUT, DELETE si tiene empresa
    GET siempre permitido
    """
    
    def has_permission(self, request, view):
        # Para métodos de lectura, permitir siempre
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        
        # Para métodos de escritura, verificar empresa
        usuario_autenticado = request.user and request.user.is_authenticated
        tiene_perfil = hasattr(request.user, 'perfil')
        tiene_empresa = tiene_perfil and request.user.perfil.empresa is not None
        
        return bool(usuario_autenticado and tiene_perfil and tiene_empresa)
    
    def has_object_permission(self, request, view, obj):
        # Para lectura, permitir siempre
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Para escritura, verificar empresa
        if hasattr(obj, 'empresa'):
            return obj.empresa == request.user.perfil.empresa
        
        return False