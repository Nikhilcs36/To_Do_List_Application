from rest_framework import serializers
from .models import TodoItem, Tag
from django.utils import timezone


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


def valid_len(value):
    if len(value) < 2:
        raise serializers.ValidationError('too short')
    else:
        return value


class TodoItemSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[valid_len])
    description = serializers.CharField(validators=[valid_len])
    tags = serializers.SlugRelatedField(many=True, slug_field='value', queryset=Tag.objects.all())

    class Meta:
        model = TodoItem
        fields = '__all__'

    def validate_title(self, value):  # field level validation
        if not value[0].isupper():
            raise serializers.ValidationError('Title must be start with a capital letter')
        else:
            return value

    def validate(self, data):     # object level validation
        if data['title'] == data['description']:
            raise serializers.ValidationError('title and description can not be same')

#  check if due date is before time created
        timestamp_created = self.instance.timestamp if self.instance else timezone.now()
        due_date = data.get('due_date')
        if due_date and due_date < timestamp_created.date():
            raise serializers.ValidationError('Due Date Cannot be before Time stamp created')
        return data
