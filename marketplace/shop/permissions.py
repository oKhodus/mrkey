from rest_framework import permissions

class IsAuthor(permissions.BasePermission):
    """
    Custom permissions to only allow authors to edit their products
    """
    def has_object_permission(self, request, view, obj):
        """
        make a permission only if user is author
        """
        return obj.author == request.user