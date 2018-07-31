from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag
@stringfilter
def get_document_name(document_relative_dir):
    return document_relative_dir.split('/')[-1]