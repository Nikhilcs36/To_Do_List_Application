from rest_framework import serializers
from .models import TodoItem, Tag, ProgressNote
from django.utils import timezone
from django.urls import reverse


def valid_len(value):
    if len(value) < 2:
        raise serializers.ValidationError('too short')
    else:
        return value
    

class ProgressNoteSerializer(serializers.ModelSerializer):
    todotask = serializers.StringRelatedField(read_only=True)
    author = serializers.ReadOnlyField(source='author.username') # Retrieve username attribute from the related User object
    class Meta:
        model = ProgressNote
        fields = '__all__'
    
    
    
class TodoItemSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    title = serializers.CharField(validators=[valid_len])
    description = serializers.CharField(validators=[valid_len])
    tags = serializers.SlugRelatedField(many=True, slug_field='tag_name', queryset=Tag.objects.all())
    progress_note = serializers.SerializerMethodField()

    class Meta:
        model = TodoItem
        fields = '__all__'
        
    def get_progress_note(self, obj):
        progress_note = ProgressNote.objects.filter(todotask=obj).order_by('-date_created')[:2]
        request = self.context.get('request')
        if progress_note.exists():
            return {
                "progress_note": ProgressNoteSerializer(progress_note, many=True).data,
                "all_progress_note_link": request.build_absolute_uri(reverse('progress_note_list', kwargs={'todotask_id':obj.id}))
            }
        else:
            return None

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
    author = serializers.StringRelatedField(read_only=True)
    tag_name = serializers.CharField()
    todo = TodoItemSerializer(many=True, read_only=True)
    class Meta:
        model = Tag
        fields = '__all__'
    
    def validate_tag_name(self, value):  # field level validation
        if not value[0].isupper():
            raise serializers.ValidationError('Tag_name must be start with a capital letter')
        else:
            return value