"""from rest_framework import permissions"""


"""проверка является ли пользователь владельцем тикета,если да
то пользователь может обновлять и удалять тикет,в противном случае только 
прочитать """
"""class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user"""
    