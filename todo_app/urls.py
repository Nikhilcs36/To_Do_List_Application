from django.urls import path
from todo_app import views

urlpatterns = [
    path('api/todo_list/', views.TodoListCreateView.as_view(), name='todo_list'),
    path('api/todo_detail/<int:pk>/', views.TodoDetailView.as_view(), name='todo_detail'),
    path('api/tag_list/',views.TagListCreateView.as_view(), name='tag_list'),
    path('api/tag_detail/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),
    
    
  
]
