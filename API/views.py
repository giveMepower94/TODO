from rest_framework import generics, permissions, viewsets
from API.serializers import TodoListSerializer, TodoItemSerializer
from tasks.models import TodoList, TodoItem
from API.permissions import IsOwner, IsListOwner


# Create your views here.
class TodoListListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def filter_queryset(self, queryset):
        return queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoListRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class TodoItemViewsets(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer
    queryset = TodoItem.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsListOwner]

    def filter_queryset(self, queryset):
        return queryset.filter(todo_list__owner=self.request.user)
