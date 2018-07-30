from django import template
from tracks.models import CompletedTopic

register = template.Library()

@register.filter
def get_track_progress(track, user):
    try:
        return round(len(CompletedTopic.objects.filter(
                    user=user, topic__track__slug=track.slug
                )) / track.number_of_topics * 100, 2)
    except:
        return 0.0;