from rest_framework import permissions

class VeterinariaPermisos(permissions.BasePermission):
    """
    Docstring for VeterinariaPermisos
    """
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            hasattr(request.user, 'empresa') and 
            request.user.empresa
        )
    
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'empresa'):
            return obj.empresa == request.user.empresa
        return False