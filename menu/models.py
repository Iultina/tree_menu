from django.db import models

class MenuItem(models.Model):
   title = models.CharField(max_length=255)
   url = models.CharField(max_length=255, blank=True)
   named_url = models.CharField(max_length=255, blank=True)
   parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
   menu_name = models.CharField(max_length=255, help_text="Название меню, например 'main_menu'")

   def __str__(self):
       return self.title