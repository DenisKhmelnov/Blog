from rest_framework import permissions

from posts.models import User


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, User):
            return obj == request.user
