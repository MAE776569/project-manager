from django import forms
from .models import Track, Topic

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['title', 'description']
        help_texts = {
            'title': "Title must be unique for track.",
            'description': "Add a detailed description to the track."
        }

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description']
        help_texts = {
            'title': "Title must be unique for topic.",
            'description': "Add a detailed description to the topic."
        }