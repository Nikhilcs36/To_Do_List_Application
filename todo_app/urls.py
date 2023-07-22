from django.urls import path
from todo_app import views

urlpatterns = [
    path('api/todo_list/', views.TodoListCreateView.as_view(), name='todo_list'),
    path('api/todo_detail/<int:pk>/', views.TodoDetailView.as_view(), name='todo_detail'),
    path('api/tag_list/',views.TagListCreateView.as_view(), name='tag_list'),
    path('api/tag_detail/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),
    path('api/progress_note_list/<int:todotask_id>/', views.ProgressNoteListCreateView.as_view(), name='progress_note_list'),
    path('api/progress_note_detail/<int:todotask_id>/<int:progress_note_id>/', views.ProgressNoteDetailView.as_view(), name='progress_note_detail'),
  
]
