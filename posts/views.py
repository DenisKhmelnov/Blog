from datetime import date
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from posts.models import User, Post, Comment
from posts.permissions import IsOwner
from posts.serializers import UserSerializer, PostSerializer, CommentSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action in ['retrieve', 'list']:
            permission_classes = [IsAuthenticated | IsAdminUser]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [IsOwner]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        birth_date = request.user.birth_date
        title: str = request.data.get("title")

        if birth_date:
            age = date.today().year - birth_date.year  # Вычисляем возраст в годах
            if age < 18:
                raise ValidationError("Вы должны быть старше 18 лет, чтобы создавать посты.")

        for word in ["ерунда", "глупость", "чепуха"]:
            if word in title:
                raise ValidationError(f"Вы использовали запрещенное слово {word}")

        return super().create(request, *args, **kwargs)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
