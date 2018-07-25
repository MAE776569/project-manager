from django.core.exceptions import PermissionDenied

def owner_required(function):
    def wrapper(request, *args, **kwargs):
        if request.user.slug != kwargs["slug"]:
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return wrapper