import locale
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, 0)

@register.filter
def format_currency(value):
    try:
        value = float(value)
        return "${:,.0f}".format(value)
    except (ValueError, TypeError):
        return "$0 COP"
