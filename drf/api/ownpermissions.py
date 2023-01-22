from rest_framework import permissions

class ProfilePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # 新規作成や取得を含む
            return True
        return False
