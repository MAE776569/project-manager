from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Track, Topic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from administrator.decorators import admin_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from .forms import TrackForm
from django.contrib import messages
from django.shortcuts import get_object_or_404

class TracksList(LoginRequiredMixin, ListView):
    model = Track
    context_object_name = 'tracks'
    template_name = 'tracks/tracks-list.html'
    paginate_by = 5

    def get_queryset(self):
        return Track.objects.all().order_by('created_at')

class CreateTrack(LoginRequiredMixin, CreateView):
    model = Track
    template_name = 'tracks/track-form.html'
    form_class = TrackForm

    @method_decorator(admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Add track"
        return context

    def get_success_url(self):
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.success(self.request, "A new track has been added successfully.")
        return reverse('tracks:tracks-list')

class EditTrack(LoginRequiredMixin, UpdateView):
    model = Track
    template_name = 'tracks/track-form.html'
    form_class = TrackForm

    @method_decorator(admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edit track"
        return context

    def get_success_url(self):
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.success(self.request, "Track has been updated successfully.")
        return reverse('tracks:tracks-list')

class DeleteTrack(LoginRequiredMixin, DeleteView):
    model = Track
    template_name = 'tracks/confirm-delete.html'

    @method_decorator(admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.success(self.request, "Track has been deleted successfully.")
        return reverse('tracks:tracks-list')

class TopicsList(LoginRequiredMixin, ListView):
    model = Topic
    context_object_name = 'topics'
    template_name = 'topics/topics-list.html'
    paginate_by = 5

    def get_queryset(self):
        track = get_object_or_404(Track, slug=self.kwargs['slug'])
        return Topic.objects.filter(track=track).order_by('created_at')

#TODO: add create view and override get_object