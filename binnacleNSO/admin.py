from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.Alias)
admin.site.register(models.Entry)