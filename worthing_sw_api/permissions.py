from rest_framework import permissions


class IsUserOrReadOnly(permissions.BasePermission):
    """Custom permission, allows read-only requests for all users and write requests
    for only the user who is the owner of the given obj.
    Unlike permissions.IsAuthenticatedOrReadOnly, checks the user is the specific user
    related to the obj, rather than accepted any authenticated user.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
