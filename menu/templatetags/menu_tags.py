from django import template
from menu.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu.html')
def draw_menu(menu_name):
   root_items = MenuItem.objects.filter(menu_name=menu_name, parent=None)
   return {'items': root_items}