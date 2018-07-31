from django import forms
from .models import Link, Document

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = '__all__'

        help_texts = {
            'title': "The title of the link.",
            'subtitle': "The subtitle that briefly describes the link.",
            'url': "The href of the link."
        }

class DocumentCreateForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        help_texts = {
            'title': "The title of the document.",
            'subtitle': "The subtitle that briefly describes the document.",
            'document': "The file to upload."
        }

class DocumentUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['document'].required = False

    class Meta:
        model = Document
        fields = '__all__'
        help_texts = {
            'title': "The title of the document.",
            'subtitle': "The subtitle that briefly describes the document.",
            'document': "The file to upload."
        }