from django.contrib import admin

# Register your models here.
from . import models


class UserManager(admin.ModelAdmin):
    list_display = ['id', 'username', 'password']


admin.site.register(models.User, UserManager)
