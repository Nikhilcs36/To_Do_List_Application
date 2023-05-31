from django.contrib import admin
from .models import TodoItem, Tag


class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'description')
    fieldsets = (
        ('Task Details', {'fields': ('title', 'description')}),
        ('Additional Info', {'fields': ('due_date', 'tags', 'status')}),
    )
    readonly_fields = ('timestamp',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(TodoItem)
admin.site.register(Tag)
