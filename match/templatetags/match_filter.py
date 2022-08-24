from django import template
from datetime import datetime

register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg

@register.filter
def current_date():
    return datetime.now()
