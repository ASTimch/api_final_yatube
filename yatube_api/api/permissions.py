from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow post author to edit it.
    Assumes the Post instance has an `author` attribute.
    """

    def has_permission(self, request, view):
        # Read available for anonimous, write only for authenticated
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request.
        # UNSAFE methods available only for `author`.
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
