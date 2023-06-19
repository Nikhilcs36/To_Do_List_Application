from rest_framework import generics
from .models import TodoItem, Tag, ProgressNote
from .serializers import TodoItemSerializer, TagSerializer, ProgressNoteSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TagSerializer(queryset, many=True, context={'request':request})
        
        if queryset.exists():
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'message':'No Tag Found in the database'})
        
    def create(self, request, *args, **kwargs):
        serializer = TagSerializer(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
    def get_object(self):
        try:  # Try to retrieve the object using the parent class method
            return super().get_object() 
        except Http404:
            return None # If object is not found, return None instead of raising Http404
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        
        if instance is not None:
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message':'No Tag found in the database'}, status=status.HTTP_404_NOT_FOUND)
    

    
class TodoListCreateView(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    
    def list(self, request , *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TodoItemSerializer(queryset, many=True, context={'request':request})
        
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message':'No items in the database'}, status=status.HTTP_204_NO_CONTENT)
        
    def create(self, request, *args, **kwargs):
        serializer = TodoItemSerializer(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
    
class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    # lookup_field ='id'
    
    def get_object(self):
        try:  # Try to retrieve the object using the parent class method
            return super().get_object() 
        except Http404:
            return None # If object is not found, return None instead of raising Http404
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        
        if instance is not None:
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message':'No items found in the database'}, status=status.HTTP_404_NOT_FOUND)
        
        
class ProgressNoteListCreateView(generics.ListCreateAPIView):
    queryset = ProgressNote.objects.all()
    serializer_class =ProgressNoteSerializer
    
    def get_queryset(self):
        todotask_id = self.kwargs.get('todotask_id')
        return ProgressNote.objects.filter(todotask_id=todotask_id)
    
    def perform_create(self, serializer):
        todotask_id = self.kwargs.get('todotask_id')
        todotask = get_object_or_404(TodoItem, id=todotask_id)
        serializer.save(author=self.request.user, todotask=todotask)
        