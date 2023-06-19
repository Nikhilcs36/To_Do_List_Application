from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class TodoItem(models.Model):
    objects = None  # added for avoid Unresolved attribute reference 'objects' 
    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('WORKING', 'working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    )

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    due_date = models.DateField(blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # Check if the due_date exists and if it has passed the current date
        if self.due_date and self.due_date < timezone.now().date():
            self.status = 'OVERDUE'    # Update the status before saving
        super().save(*args, **kwargs)


class Tag(models.Model):
    objects = None
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.tag_name
