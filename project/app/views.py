from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.contrib.auth.models import User
from app.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated,BasePermission
from rest_framework.exceptions import PermissionDenied

# Create your views here.
class IsUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class UsersViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]