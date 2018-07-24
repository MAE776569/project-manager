from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Track, Topic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from administrator.decorators import admin_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from .forms import TrackForm, TopicForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.db import transaction
from django.views.decorators.csrf import ensure_csrf_cookie

class TracksList(LoginRequiredMixin, ListView):
    model = Track
    context_object_name = 'tracks'
    template_name = 'tracks/tracks-list.html'
    paginate_by = 3

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
    paginate_by = 3

    @transaction.atomic
    def get_queryset(self):
        track = get_object_or_404(Track, slug=self.kwargs['slug'])

        query = """select case when completed_topic.topic_id is null
                then false else true end completed,
                topic.* from completed_topic
                right outer join topic
                on completed_topic.topic_id=topic.id
                and completed_topic.user_id={0}
                where topic.track_id={1}
                order by
                topic.created_at;""".format(self.request.user.id, track.id)
        return list(Topic.objects.raw(query))

class AddTopic(LoginRequiredMixin, CreateView):
    model = Topic
    template_name = 'topics/topic-form.html'
    form_class = TopicForm

    @method_decorator(admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.track = get_object_or_404(Track, slug=self.kwargs['slug'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Add topic"
        return context

    def get_success_url(self):
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.success(self.request, "A new topic has been added successfully.")
        return reverse_lazy('tracks:topics',
            kwargs={
                'slug': self.kwargs['slug']
            }
        )

class EditTopic(LoginRequiredMixin, UpdateView):
    model = Topic
    template_name = 'topics/topic-form.html'
    form_class = TrackForm

    @method_decorator(admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edit topic"
        return context

    #if blank is changed in form this will be deleted
    def get_initial(self):
        initial = self.initial.copy()
        initial["video_url"] = self.object.video_url
        initial['note'] = self.object.note
        return initial

    def get_success_url(self):
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.success(self.request, "topic has been updated successfully.")
        return reverse_lazy('tracks:topics',
            kwargs={
                'slug': self.object.track.slug
            }
        )

class DeleteTopic(LoginRequiredMixin, DeleteView):
    model = Topic
    template_name = 'topics/confirm-delete.html'

    @method_decorator(admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.success(self.request, "Topic has been deleted successfully.")
        return reverse_lazy('tracks:topics',
            kwargs={
                'slug': self.object.track.slug
            }
        )

class TopicDetails(LoginRequiredMixin, ListView):
    model = Topic
    template_name = 'topics/topic-details.html'
    context_object_name = 'topic'
       
    @method_decorator(ensure_csrf_cookie)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        topic = get_object_or_404(Topic, slug=self.kwargs['slug'])
        query = """select id, prev_slug, title, description,
                    slug, next_slug, track_id
                    from (
                        select id, track_id, title, description, slug, 
                        lag(slug) over (order by created_at) as prev_slug,
                        lead(slug) over (order by created_at) as next_slug
                        from topic where track_id={0}
                    ) as anything
                    where slug='{1}';""".format(topic.track_id, self.kwargs['slug'])
        return list(Topic.objects.raw(query))