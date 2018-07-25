from django.core.exceptions import PermissionDenied

def admin_required(function):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_admin:
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return wrapper