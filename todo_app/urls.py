from django.urls import path
from todo_app import views

urlpatterns = [
    path('api/create/', views.CreateTodoItemView.as_view(), name='todo_create'),
    path('api/read/<int:pk>/', views.ReadTodoItemView.as_view(), name='todo_read'),
    path('api/read_all/', views.ReadAllTodoItemView.as_view(), name='todo_read_all'),
    path('api/update/<int:pk>/', views.UpdateTodoItemView.as_view(), name='todo_update'),
    path('api/delete/<int:pk>/', views.DeleteTodoItemView.as_view(), name='todo_create'),
]
