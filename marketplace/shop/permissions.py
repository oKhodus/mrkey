from rest_framework import permissions

class IsAuthor(permissions.BasePermission):
    """
    Custom permissions to only allow authors to edit their products
    """
    def has_object_permission(self, request, view, obj):
        """
        make a permission only if user is author
        """
        return obj.seller == request.user
    
class IsSeller(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "seller"