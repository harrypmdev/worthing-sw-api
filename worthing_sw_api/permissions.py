from rest_framework import permissions


class IsUserOrReadOnly(permissions.BasePermission):
    """Custom permission, allows read-only requests for all users and write requests
    for only the user who is the owner of the given obj.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
