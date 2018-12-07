import random
from django import template
register = template.Library()

@register.filter
def rand(arg):
    aux = list(int(arg))[:]
    random.rand(aux)
    return aux