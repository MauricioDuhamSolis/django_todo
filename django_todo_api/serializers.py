from djoser.serializers import UserCreateSerializer as BaseUserSerializer
from djoser.serializers import UserSerializer
from rest_framework import serializers

from .models import Todo


class UserCreateSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ["id", "email", "username", "password"]


class CurrentUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ["id", "email", "username", "password"]


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["task", "completed", "timestamp", "updated", "user"]
