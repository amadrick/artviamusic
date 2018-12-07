import random
from django import template
register = template.Library()

@register.filter
def rand(arg):
    aux = list(arg))[:]
    random.rand(aux)
    return aux