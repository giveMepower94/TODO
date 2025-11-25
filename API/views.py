from rest_framework import generics
from rest_framework import permissions
from API.serializers import TodoListSerializer
from tasks.models import TodoList


# Create your views here.
class TodoListListView(generics.ListAPIView):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def filter_queryset(self, queryset):
        return queryset.filter(owner=self.request.user)
