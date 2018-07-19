from django.views.generic.list import ListView
from accounts.decorators import owner_required
from .decorators import admin_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic.list import ListView

class TrustedUsers(LoginRequiredMixin, ListView):
    model = get_user_model()
    context_object_name = 'trusted_users'
    template_name = 'accounts/trusted-users.html'
    paginate_by = 10

    @method_decorator(admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return get_user_model().objects.filter(is_admin=False).order_by('name')