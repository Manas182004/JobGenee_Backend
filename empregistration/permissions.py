#empregistration/permissions.py

from rest_framework.permissions import BasePermission

class IsEmployerUser(BasePermission):
    """
    Allows access only to users with the employer role.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and hasattr(request.user, 'emp_profile') and request.user.emp_profile.role == 'employer'