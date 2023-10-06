from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
   list_display = ['title', 'url', 'named_url', 'parent', 'menu_name']
   list_filter = ['menu_name']

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)