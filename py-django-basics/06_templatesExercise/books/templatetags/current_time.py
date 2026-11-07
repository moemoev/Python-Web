from django import template
from django.utils.timezone import now

register = template.Library()

@register.simple_tag
def current_time():
    return now()