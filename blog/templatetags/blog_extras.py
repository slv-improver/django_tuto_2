from django import template
from django.utils import timezone


register = template.Library()

@register.filter
def model_type(instance):
    return type(instance).__name__

@register.simple_tag(takes_context=True)
def get_poster_display(context, user):
    if user == context['user']:
        return 'me'
    return user.username

@register.filter
def get_posted_at_display(time):
    posted_before = timezone.now() - time # .total_seconds() to work with delta in sec
    if posted_before.days > 0:
        return f'at {time.strftime("%H:%M %d-%b-%y")}'
    elif posted_before.seconds > 3599:
        return f'before {posted_before.seconds // 3600} h'
    else:
        return f'before {posted_before.seconds // 60} min'
