from django import template
from ..models import CompletedTopic

register = template.Library()

@register.filter
def get_track_progress(track, user):
    return round(len(CompletedTopic.objects.filter(
                user=user, topic__track__slug=track.slug
            )) / track.number_of_topics * 100, 2)