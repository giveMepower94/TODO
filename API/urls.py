from django.urls import path
from API.views import TodoListListView


urlpatterns = [
    path("lists/", TodoListListView.as_view())
]
