from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from posts.models import User, Post, Comment
from posts.validators import password_validator, mail_validator, age_validator


class UserSerializer(ModelSerializer):
    password = serializers.CharField(validators=[password_validator])
    email = serializers.CharField(validators=[mail_validator])
    birth_date = serializers.DateField(validators=[age_validator])

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(user.password)
        user.save()

        return user

    class Meta:
        model = User
        fields = ["phone", "birth_date", "username", "password", "email"]


class PostSerializer(ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Comment
        fields = "__all__"
