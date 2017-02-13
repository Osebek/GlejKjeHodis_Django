from rest_framework import permissions
from django.contrib.auth.models import User

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class UserPermissionsDetail(permissions.BasePermission):
    def has_object_permission(self,request,view):
        return False
