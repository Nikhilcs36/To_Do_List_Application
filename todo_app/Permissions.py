from rest_framework import permissions

class IsOwnerOrSuperuser(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
        if request.user.is_superuser:
            return True
        
        if request.method in permissions.SAFE_METHODS and obj.author == request.user:
            return True
        
        return obj.author == request.user