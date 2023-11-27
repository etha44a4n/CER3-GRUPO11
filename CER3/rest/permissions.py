from rest_framework import permissions

class IsDeveloper(permissions.BasePermission):
    #Para ver la solicitud
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True 
        elif request.user.is_authenticated and str(request.user.tipo_cuenta) == 'Developer':
            return True 
        return False

    #Para ver la opción
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True 
        elif request.user.is_authenticated and str(request.user.tipo_cuenta) == 'Developer':
            return True 
        return False