from django.core.exceptions import PermissionDenied

def owner_or_admin_required(function):
    def wrapper(request, *args, **kwargs):
        user_slug = kwargs.get("slug") or kwargs.get('user_slug')
        if not request.user.is_admin and request.user.slug != user_slug:
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return wrapper