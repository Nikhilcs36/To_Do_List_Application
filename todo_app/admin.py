from django.contrib import admin
from .models import TodoItem, Tag


class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'timestamp', 'due_date', 'status')
    list_filter = ('status',)
    search_fields = ('id', 'title', 'description')
    readonly_fields = ('timestamp',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name','author')


admin.site.register(TodoItem, TodoItemAdmin)
admin.site.register(Tag, TagAdmin)
