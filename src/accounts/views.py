from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .decorators import owner_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import PasswordChangeView
from .forms import UserChangePasswordForm
from django.urls import reverse_lazy
from django.contrib import messages

class UserProfile(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'accounts/profile.html'
    context_object_name = "user"

    @method_decorator(owner_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class PasswordChange(PasswordChangeView):
    template_name = 'accounts/password-change.html'
    form_class = UserChangePasswordForm
    success_url = "/"

    @method_decorator(owner_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)