from django import template

register = template.Library()

@register.filter
def count_unseen(notifs):
    count = 0
    for notif in notifs:
        count += int(not notif.seen)
    return count