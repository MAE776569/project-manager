from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag
@stringfilter
def media_avatars(image_relative_dir):
    return "{}{}".format('/media/', image_relative_dir)