from django.db import models
from django.utils import timezone


class TodoItem(models.Model):
    objects = None  # added for avoid Unresolved attribute reference 'objects' 
    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('WORKING', 'working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    )

    timestamp = models.DateTimeField(auto_now_add=True)
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
    value = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.value
