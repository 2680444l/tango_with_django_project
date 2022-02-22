from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/categories.html')
# this method returns a dictionary with one key/value pairing
def get_category_list():
    return {'categories': Category.objects.all()}