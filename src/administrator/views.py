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
from django.urls import reverse
from django.contrib import messages

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

    #TODO: send email when the form is valid for verification

    def get_success_url(self):
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.success(self.request, "New account verification has been added successfully.")
        return reverse("accounts:account-verifications")