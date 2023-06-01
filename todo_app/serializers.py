from rest_framework import serializers
from .models import TodoItem, Tag


def valid_len(value):
    if len(value) < 2:
        raise serializers.ValidationError('too short')
    else:
        return value


class TodoItemSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[valid_len])
    description = serializers.CharField(validators=[valid_len])

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
        else:
            return data


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
