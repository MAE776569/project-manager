from django.shortcuts import HttpResponse

def admin_required(function):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_admin:
            return HttpResponse(status=401)
        return function(request, *args, **kwargs)
    return wrapper