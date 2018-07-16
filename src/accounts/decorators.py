from django.shortcuts import HttpResponse

def owner_required(function):
    def wrapper(request, *args, **kwargs):
        if request.user.slug != kwargs["slug"]:
            return HttpResponse(status=401)
        return function(request, *args, **kwargs)
    return wrapper