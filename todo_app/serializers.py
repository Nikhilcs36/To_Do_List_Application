from rest_framework import serializers
from .models import TodoItem, Tag
from django.utils import timezone

def valid_len(value):
    if len(value) < 2:
        raise serializers.ValidationError('too short')
    else:
        return value
    
class TodoItemSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    title = serializers.CharField(validators=[valid_len])
    description = serializers.CharField(validators=[valid_len])
    tags = serializers.SlugRelatedField(many=True, slug_field='tag_name', queryset=Tag.objects.all())

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


class TagSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    todo = TodoItemSerializer(many=True)
    class Meta:
        model = Tag
        fields = '__all__'
    
    def validate_tag_name(self, value):  # field level validation
        if not value[0].isupper():
            raise serializers.ValidationError('Tag_name must be start with a capital letter')
        else:
            return value