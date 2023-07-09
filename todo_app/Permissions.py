from rest_framework import permissions
from django.shortcuts import get_object_or_404
from . models import TodoItem
from rest_framework.exceptions import NotFound

class IsOwnerOrSuperUserReadonly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj): 
        
        if request.method in permissions.SAFE_METHODS and obj.author == request.user:  # Check if the request method is safe (GET, HEAD, OPTIONS) and the object's author is the same as the requesting user.
            return True
        
        if request.user.is_superuser and obj.author != request.user:  # Check if the requesting user is a superuser (admin), but not the author of the object. Allow safe methods (read-only) for admin users who are not the authors.    
            return request.method in permissions.SAFE_METHODS
        
        return obj.author == request.user  # Allow unsafe methods (e.g., create, update, delete) only if the object's author is the same as the requesting user.
    
class IsOwnerOrSuperUserReadonlyProgressNote(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        todotask_id = view.kwargs.get('todotask_id')
        try:
            todotask = get_object_or_404(TodoItem, id=todotask_id)
        except:
            raise NotFound("Todo item does not exist")
        
        progressnote_author = todotask.author
        
        if request.method in permissions.SAFE_METHODS and progressnote_author == request.user:
            return True
        
        if request.user.is_superuser and progressnote_author != request.user:
            return request.method in permissions.SAFE_METHODS
        
        return progressnote_author == request.user