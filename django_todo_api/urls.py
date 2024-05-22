from django.urls import include, path

from .views import TodoListAPIView

urlpatterns = [path("api", TodoListAPIView.as_view())]
