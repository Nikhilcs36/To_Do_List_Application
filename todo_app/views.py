from rest_framework import generics
from .models import TodoItem, Tag, ProgressNote
from .serializers import TodoItemSerializer, TagSerializer, ProgressNoteSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .Permissions import IsOwnerOrSuperUserReadonlyTodoDetail, IsOwnerOrSuperUserReadonlyTagDetail, IsOwnerOrSuperUserReadonlyProgressNote, IsOwnerOrSuperUserReadonlyProgressNoteDetail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from . pagination import TodoListCreatePagination, ListPagination

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tag_name']
    pagination_class = ListPagination
    
    def get_queryset(self):
        username = self.request.user
        if username.is_superuser:
            return Tag.objects.all()
        else:
            return Tag.objects.filter(author=username)
    
    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = TagSerializer(queryset, many=True, context={'request':request})
        
    #     if queryset.exists():
    #         return Response(serializer.data,status=status.HTTP_200_OK)
    #     else:
    #         return Response({'message':'No Tag Found in the database'})
        
    def create(self, request, *args, **kwargs):
        serializer = TagSerializer(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrSuperUserReadonlyTagDetail]
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            return Response({'message': 'No items found in the database'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class TodoListCreateView(generics.ListCreateAPIView):
    # queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['tags', 'status']
    search_fields = ['^title']
    ordering_fields = ['timestamp','due_date']
    pagination_class = TodoListCreatePagination
    
    def get_queryset(self):
        username = self.request.user
        if username.is_superuser:
            return TodoItem.objects.all()
        else:
            return TodoItem.objects.filter(author=username)
    
    # def list(self, request , *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = TodoItemSerializer(queryset, many=True, context={'request':request})
        
    #     if queryset.exists():
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response({'message':'No items in the database'}, status=status.HTTP_204_NO_CONTENT)
        
    def create(self, request, *args, **kwargs):
        serializer = TodoItemSerializer(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
    
class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrSuperUserReadonlyTodoDetail]
    # lookup_field ='id'
        
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            return Response({'message': 'No items found in the database'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)   
  
        
class ProgressNoteListCreateView(generics.ListCreateAPIView):
    # queryset = ProgressNote.objects.all()
    serializer_class =ProgressNoteSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrSuperUserReadonlyProgressNote]
    pagination_class = ListPagination
    
    
    def get_queryset(self):
        todotask_id = self.kwargs.get('todotask_id')
        username = self.request.user
        if username.is_superuser:
            queryset = ProgressNote.objects.filter(todotask_id=todotask_id)
        else:
            queryset = ProgressNote.objects.filter(todotask_id=todotask_id, author=username)
        
        # if not queryset.exists():
        #     raise NotFound(detail="No ProgressNote instances found for the provided todotask_id.")
        return queryset
    
    def perform_create(self, serializer):
        todotask_id = self.kwargs.get('todotask_id')
        todotask = get_object_or_404(TodoItem, id=todotask_id)
        
        # if todotask.author != self.request.user:
        #     raise PermissionDenied("You are not authorized to create a new progress note on this task")
        
        serializer.save(author=self.request.user, todotask=todotask)
        
        
class ProgressNoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProgressNote.objects.all()
    serializer_class = ProgressNoteSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrSuperUserReadonlyProgressNoteDetail]
    
    def get_object(self):
        progress_note_id = self.kwargs.get('progress_note_id')
        progress_note = get_object_or_404(ProgressNote, id = progress_note_id)
        
        # todotask_id = self.kwargs.get('todotask_id')
        # if progress_note.todotask.id != todotask_id:
        #     raise serializers.ValidationError({'message':'This progress note is not related to the requested todo item'})
        return progress_note