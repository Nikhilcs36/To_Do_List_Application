# Generated by Django 4.2.1 on 2023-06-19 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo_app', '0006_alter_todoitem_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgressNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('todotask', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_app.todoitem')),
            ],
        ),
    ]
