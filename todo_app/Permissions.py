from rest_framework import permissions
from django.shortcuts import get_object_or_404
from . models import TodoItem, ProgressNote, Tag
from rest_framework.exceptions import NotFound

class IsOwnerOrSuperUserReadonlyTodoDetail(permissions.BasePermission):
    
    def has_permission(self, request, view):
        todo_id = view.kwargs.get('pk')  # Get the todo_id from the view's kwargs
        try:
            todo = TodoItem.objects.get(id=todo_id) # Try to retrieve the TodoItem with the given ID
        except TodoItem.DoesNotExist:
            return request.method in permissions.SAFE_METHODS and request.user.is_superuser  # Return True for safe methods and superusers, False for other methods and non-superusers
        
        author = getattr(todo, 'author', None)  # Get the author of the TodoItem
        
        if request.user.is_superuser and author != request.user: 
            return request.method in permissions.SAFE_METHODS  # Allow safe methods for superusers who are not the authors
        
        return author == request.user
    
    
class IsOwnerOrSuperUserReadonlyTagDetail(permissions.BasePermission):
    
    def has_permission(self, request, view):
        tag_id = view.kwargs.get('pk')
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            return request.method in permissions.SAFE_METHODS and request.user.is_superuser
        
        author = getattr(tag, 'author', None)
        
        if request.user.is_superuser and author != request.user:  # Allow safe methods if the user is a superuser and not the author
            return request.method in permissions.SAFE_METHODS
        
        return author == request.user


class IsOwnerOrSuperUserReadonlyProgressNote(permissions.BasePermission):
    
    def has_permission(self, request, view):
        todotask_id = view.kwargs.get('todotask_id')
        
        try:
            todotask = get_object_or_404(TodoItem, id=todotask_id)  # Try to retrieve the TodoItem with the given ID
        except:
            if request.user.is_superuser:
                raise NotFound("Todo item does not exist")  # Raise NotFound exception if TodoItem doesn't exist and user is a superuser
            return False  # Deny access if TodoItem doesn't exist and user is not a superuser
        
        progressnote_author = todotask.author
        
        if request.user.is_superuser and progressnote_author != request.user:  # Allow safe methods if the user is a superuser and not the progress note author
            return request.method in permissions.SAFE_METHODS
        
        return progressnote_author == request.user  # Allow access if the user is the progress note author
   
    
class IsOwnerOrSuperUserReadonlyProgressNoteDetail(permissions.BasePermission):
    
    def has_permission(self, request, view):
        todotask_id = view.kwargs.get('todotask_id')
        progress_note_id = view.kwargs.get('progress_note_id')
        
        try:
            progress_note = ProgressNote.objects.get(id=progress_note_id)
        except:
            if request.user.is_superuser:
                raise NotFound("Progress note does not exist")  # Raise NotFound exception if progress note doesn't exist and user is a superuser
            return False  # Deny access if progress note doesn't exist and user is not a superuser

        if progress_note.todotask.id != todotask_id:
            if request.user.is_superuser:
                raise NotFound("This progress note id is not related to the requested todo item")  # Raise NotFound exception if progress note is not related to the requested todo item and user is a superuser
            return False  # Deny access if progress note is not related to the requested todo item and user is not a superuser
        
        progressnote_author = progress_note.todotask.author  # Get the author of the progress note
        
        if request.user.is_superuser and progressnote_author != request.user:  # Allow safe methods if the user is a superuser and not the progress note author
            return request.method in permissions.SAFE_METHODS
        
        return progressnote_author == request.user  # Allow access if the user is the progress note author
    
    
    