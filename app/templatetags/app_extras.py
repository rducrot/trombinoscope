from django import template

register = template.Library()


@register.filter
def sort_list(value):
    return sorted(value, reverse=True)

