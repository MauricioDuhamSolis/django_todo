from django.urls import path, include
from .views import TodoListAPIView

urlpatterns = [path("api", TodoListAPIView.as_view())]
