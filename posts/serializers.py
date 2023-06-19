from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from posts.models import User, Post, Comment
from posts.validators import password_validator, mail_validator


class UserSerializer(ModelSerializer):
    password = serializers.CharField(validators=[password_validator])
    email = serializers.CharField(validators=[mail_validator])

    class Meta:
        model = User
        fields = ["phone", "birth_date", "username", "password", "email"]


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
