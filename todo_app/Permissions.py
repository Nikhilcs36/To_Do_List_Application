from rest_framework import permissions

class IsOwnerOrSuperUserReadonly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj): # Check if the request method is safe (GET, HEAD, OPTIONS) and the object's author is the same as the requesting user.
        
        if request.method in permissions.SAFE_METHODS and obj.author == request.user:  # Check if the requesting user is a superuser (admin), but not the author of the object.
            return True
        
        if request.user.is_superuser and obj.author != request.user: # Allow safe methods (read-only) for admin users who are not the authors.     
            return request.method in permissions.SAFE_METHODS
        
        return obj.author == request.user  # Allow unsafe methods (e.g., create, update, delete) only if the object's author is the same as the requesting user.