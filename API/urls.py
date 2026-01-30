from django.urls import path, include
from API.views import (TodoListListCreateView,
                       TodoListRetrieveUpdateDestroyView,
                       TodoItemViewsets)
from rest_framework import routers

router = routers.DefaultRouter()
router.register("items", viewset=TodoItemViewsets, basename="item")

urlpatterns = [
    path("", include(router.urls)),
    path("lists/", TodoListListCreateView.as_view()),
    path("lists/<int:pk>/", TodoListRetrieveUpdateDestroyView.as_view()),
]
