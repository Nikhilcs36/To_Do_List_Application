from rest_framework import generics
from .models import TodoItem
from .serializers import TodoItemSerializer


class CreateTodoItemView(generics.CreateAPIView):  # CREATE
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


class ReadTodoItemView(generics.RetrieveAPIView):  # READ ONE
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


class ReadAllTodoItemView(generics.ListAPIView):  # READ ALL
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


class UpdateTodoItemView(generics.UpdateAPIView):  # UPDATE
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


class DeleteTodoItemView(generics.DestroyAPIView):  # DELETE
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
