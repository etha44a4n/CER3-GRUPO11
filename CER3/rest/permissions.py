from rest_framework import permissions

class IsDeveloper(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if str(request.user.tipo_cuenta) == 'Developer':
                return True
        return False