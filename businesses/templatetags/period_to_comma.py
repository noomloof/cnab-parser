from django import template

register = template.Library()

@register.filter
def period_to_comma(value):
        string = str(value)
        return string.replace('.',',')
