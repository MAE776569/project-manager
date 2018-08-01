from django.views.generic.list import ListView
from administrator.decorators import admin_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Link, Document
from itertools import chain
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from .forms import (LinkForm, DocumentCreateForm, DocumentUpdateForm,
SearchResourcesForm)

class ResourcesList(LoginRequiredMixin, ListView):
    model = Link
    context_object_name = 'resources'
    template_name = 'resources/resources-list.html'
    paginate_by = 3

    def get_queryset(self):
        form = SearchResourcesForm(self.request.GET)
        if form.is_valid():
            resource_name = form.cleaned_data.get('resource_name')
            resource_type = form.cleaned_data.get('resource_type')
            links, documents = [], []

            if resource_type:
                if 'link' in resource_type:
                    links = Link.objects.filter(title__icontains=resource_name)
                if 'document' in resource_type:
                    documents = Document.objects.filter(title__icontains=resource_name)
                
            else:
                links = Link.objects.filter(title__icontains=resource_name)
                documents = Document.objects.filter(title__icontains=resource_name)

        else:
            links = Link.objects.all()
            documents = Document.objects.all()
        
        return list(chain(links, documents))

class AddLink(LoginRequiredMixin, CreateView):
    model = Link
    template_name = 'resources/link-form.html'
    form_class = LinkForm

    @method_decorator(admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Link'
        return context

    def get_success_url(self):
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.success(self.request, "New link has been added successfully.")
        return reverse("resources:resources-list")

class UpdateLink(LoginRequiredMixin, UpdateView):
    model = Link
    template_name = 'resources/link-form.html'
    form_class = LinkForm

    @method_decorator(admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Link'
        return context

    def get_success_url(self):
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.success(self.request, "Link has been updated successfully.")
        return reverse("resources:resources-list")

class DeleteLink(LoginRequiredMixin, DeleteView):
    model = Link
    template_name = 'resources/confirm-delete-link.html'

    @method_decorator(admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.success(self.request, "Link has been deleted successfully.")
        return reverse("resources:resources-list")

class AddDocument(LoginRequiredMixin, CreateView):
    model = Document
    template_name = 'resources/document-form.html'
    form_class = DocumentCreateForm

    @method_decorator(admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Document'
        return context

    def get_success_url(self):
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.success(self.request, "New document has been added successfully.")
        return reverse("resources:resources-list")

class UpdateDocument(LoginRequiredMixin, UpdateView):
    model = Document
    template_name = 'resources/document-form-update.html'
    form_class = DocumentUpdateForm

    @method_decorator(admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Document'
        return context

    def get_success_url(self):
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.success(self.request, "Document has been updated successfully.")
        return reverse("resources:resources-list")

class DeleteDocument(LoginRequiredMixin, DeleteView):
    model = Document
    template_name = 'resources/confirm-delete-document.html'

    @method_decorator(admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.success(self.request, "Document has been deleted successfully.")
        return reverse("resources:resources-list")