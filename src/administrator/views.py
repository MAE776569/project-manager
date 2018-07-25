from django.views.generic.list import ListView
from accounts.decorators import owner_required
from .decorators import admin_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from authentication.models import AccountVerification
from .forms import AddAccountVerificationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.core.exceptions import PermissionDenied

class AccountVerificationsList(LoginRequiredMixin, ListView):
    model = AccountVerification
    context_object_name = 'account_verifications'
    template_name = 'admin/account-verifications.html'
    paginate_by = 10

    @method_decorator(admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return AccountVerification.objects.all().order_by('name')

class AddAccountVerification(LoginRequiredMixin, CreateView):
    model = AccountVerification
    template_name = 'admin/add-account-verification.html'
    form_class = AddAccountVerificationForm

    @method_decorator(admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy("accounts:verification-link", kwargs={
            'slug': str(self.object.uuid)
        })

class VerificationLink(LoginRequiredMixin, DetailView):
    model = AccountVerification
    template_name = 'admin/verification-link.html'
    context_object_name = 'account'
    slug_field = 'uuid'
    
    @method_decorator(admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['verification_code'] = self.object.get_verification_code()
            return context
        except ValueError:
            raise PermissionDenied

class UsersList(LoginRequiredMixin, ListView):
    model = get_user_model()
    template_name = 'admin/users-list.html'
    context_object_name = 'users'

    @method_decorator(admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(is_admin=False).order_by('email')
