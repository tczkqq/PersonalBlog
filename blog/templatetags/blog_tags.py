from django import template
from ..models import Post, Tag
from django.utils.html import strip_tags

register = template.Library()

@register.filter()
def to_snippet(value, length=200):
    return strip_tags(value[:length]) + '...'
