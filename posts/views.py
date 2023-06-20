from datetime import date

from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from posts.models import User, Post, Comment
from posts.serializers import UserSerializer, PostSerializer, CommentSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        birth_date = request.user.birth_date

        if birth_date:
            age = date.today().year - birth_date.year  # Вычисляем возраст в годах
            if age < 18:
                raise ValidationError("Вы должны быть старше 18 лет, чтобы создавать посты.")

        return super().create(request, *args, **kwargs)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



class LogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
