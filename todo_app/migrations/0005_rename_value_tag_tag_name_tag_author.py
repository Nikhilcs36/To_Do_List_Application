# Generated by Django 4.2.1 on 2023-06-19 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo_app', '0004_todoitem_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='value',
            new_name='tag_name',
        ),
        migrations.AddField(
            model_name='tag',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]