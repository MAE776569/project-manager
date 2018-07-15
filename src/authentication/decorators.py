from django.shortcuts import redirect, HttpResponse
from .models import AccountVerification
from django.contrib import messages

def user_authenticated_redirect(function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            storge = messages.get_messages(request)
            storge.used = True
            messages.info(request, "You are already Logged in.")
            return redirect("accounts:profile", slug=request.user.slug)
        return function(request, *args, **kwargs)
    return wrapper

def verify_account(function):
    def wrapper(request, *args, **kwargs):
        verification_code = request.GET.get('vfc', None)
        uuid = request.GET.get('uid', None)
        if not verification_code or not uuid:
            return HttpResponse(status=401)
        verified_account = None
        try:
            verified_account = AccountVerification.objects.get(uuid=uuid)
            if verified_account.verified or not verified_account.verify_code(verification_code):
                return HttpResponse(status=401)
            else:
                verified_account.verified = True
                verified_account.save()
        except:
            return HttpResponse(status=401)
        return function(request, *args, **kwargs)
    return wrapper

def verify_user_account(function):
    def wrapper(request, *args, **kwargs):
        uuid = request.GET.get("uid", None)
        if not uuid:
            return HttpResponse(status=401)
        try:
            verified_account = AccountVerification.objects.get(uuid=uuid)
            if not verified_account.verified:
                return HttpResponse(status=401)
        except:
            return HttpResponse(status=401)
        return function(request, *args, **kwargs)
    return wrapper