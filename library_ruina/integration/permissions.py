from rest_framework import permissions
from .models import TokenImport


class SuccessToken(permissions.BasePermission):
    """Проверка валидности token"""

    def has_permission(self, request, view):
        token = request.GET.get("token")
        return TokenImport.objects.filter(token=token).exists()

