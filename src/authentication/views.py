from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm, RegistrationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .decorators import user_authenticated_redirect, verify_account, verify_user_account
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.generic import TemplateView
from django.db import transaction
from django.shortcuts import HttpResponse, HttpResponseRedirect
from .models import AccountVerification
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

class Login(LoginView):
    template_name = 'auth/login.html'
    form_class = LoginForm

    @method_decorator(user_authenticated_redirect)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self, *args, **kwargs):
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.success(self.request, "Logged in successfully.")
        return reverse_lazy("accounts:profile", kwargs={
                'slug': self.request.user.slug
            })

class Registration(CreateView):
    template_name = 'auth/register.html'
    form_class = RegistrationForm
    
    @transaction.atomic
    @method_decorator(verify_user_account)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @transaction.atomic
    def form_valid(self, form):
        email = form.cleaned_data["email"]
        uuid = self.request.GET.get("uid", None)
        if not uuid:
            return HttpResponse(status=401)
        try:
            verified_account = AccountVerification.objects.get(uuid=uuid)
            if email != verified_account.email:
                form.add_error(None, "Enter the email that was provided for verification.")
                return self.form_invalid(form)
        except:
            return HttpResponse(status=401)
        self.object = form.save()
        self.object.name = verified_account.name
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @transaction.atomic
    def get_success_url(self, *args, **kwargs):
        login(self.request, self.object)
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.success(self.request, "Registered successfully.")
        return reverse_lazy("accounts:profile", kwargs={
                'slug': self.object.slug
            })

class VerifyAccount(TemplateView):
    template_name = 'auth/verify.html'

    @transaction.atomic
    @method_decorator(verify_account)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["uuid"] = self.request.GET.get("uid")
        return context

class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'

    def get_next_page(self):
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.success(self.request, "Logged out successfully.")
        return super().get_next_page()

class IndexView(TemplateView):
    template_name = 'index.html'