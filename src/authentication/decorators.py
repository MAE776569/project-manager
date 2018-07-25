from django.shortcuts import redirect
from .models import AccountVerification
from django.contrib import messages
from django.core.exceptions import PermissionDenied, ValidationError

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
            raise PermissionDenied
        verified_account = None
        try:
            verified_account = AccountVerification.objects.get(uuid=uuid)
            if verified_account.is_verified or not verified_account.verify_code(verification_code):
                raise PermissionDenied
            else:
                verified_account.is_verified = True
                verified_account.save()
        except (AccountVerification.DoesNotExist, ValueError, ValidationError) as exc:
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return wrapper

def verify_user_account_registration(function):
    def wrapper(request, *args, **kwargs):
        uuid = request.GET.get("uid", None)
        if not uuid:
            raise PermissionDenied
        try:
            verified_account = AccountVerification.objects.get(uuid=uuid)
            if not verified_account.is_verified:
                raise PermissionDenied
        except (AccountVerification.DoesNotExist, ValueError, ValidationError) as exc:
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return wrapper