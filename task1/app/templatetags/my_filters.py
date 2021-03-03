from django import template

register = template.Library()

@register.filter()

def numb(value):
    try:
        float(value)
        return float(value)
    except ValueError:
        return value