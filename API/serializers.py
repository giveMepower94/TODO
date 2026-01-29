from rest_framework import serializers
from tasks.models import TodoList, TodoItem


class TodoItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoItem
        fields = ['id', 'title', 'description', 'created_date']


class TodoListSerializer(serializers.ModelSerializer):
    items = TodoItemSerializer(many=True, read_only=True)

    class Meta:
        model = TodoList
        fields = ['id', 'title', 'owner_id', 'items']
