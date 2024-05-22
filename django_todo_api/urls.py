from django.urls import include, path

from .views import TodoDetailApiView, TodoListAPIView

urlpatterns = [
    path("api", TodoListAPIView.as_view()),
    path("api/<int:todo_id>/", TodoDetailApiView.as_view()),
]
