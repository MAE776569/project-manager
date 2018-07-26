from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .decorators import owner_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import PasswordChangeView
from .forms import UserChangePasswordForm, ProfilePictureUploadForm
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic.edit import UpdateView

class UserProfile(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'accounts/profile.html'
    context_object_name = "user_account"

    @method_decorator(owner_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class PasswordChange(PasswordChangeView):
    template_name = 'accounts/password-change.html'
    form_class = UserChangePasswordForm

    @method_decorator(owner_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.success(self.request, "Your password has been changed successfully.")
        return reverse('index')

class ProfilePictureUpload(LoginRequiredMixin, UpdateView):
    http_method_names = ['post', 'put']
    model = get_user_model()
    form_class = ProfilePictureUploadForm
    
    @method_decorator(owner_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.success(self.request, "Image has been uploaded successfully.")
        return reverse_lazy("accounts:profile", kwargs={
            'slug': self.request.user.slug
        })