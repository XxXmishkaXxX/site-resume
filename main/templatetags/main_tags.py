from django import template

register = template.Library()


@register.filter
def remove_middle_name(full_name):
    return ' '.join(full_name.split()[0:2])
