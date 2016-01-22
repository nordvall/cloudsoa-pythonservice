from datetime import datetime
from pytz import utc
from rest_framework import serializers
from models import ToDo


class ToDoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(required=True, allow_blank=False, max_length=100)
    updated_by = serializers.CharField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new ToDo instance, given the validated data.
        """
        todo = ToDo()
        todo.text = validated_data.get('text', todo.text)
        todo.updated_by = validated_data.get('updated_by', todo.updated_by)
        todo.updated_at = utc.localize(datetime.utcnow())
        return todo

    def update(self, todo, validated_data):
        """
        Update and return an existing ToDo instance, given the validated data.
        """
        todo.text = validated_data.get('text', todo.text)
        todo.updated_by = validated_data.get('updated_by', todo.updated_by)
        todo.updated_at = utc.localize(datetime.utcnow())
        return todo


class ToDoListSerializer(serializers.Serializer):
    items = ToDoSerializer(many=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass