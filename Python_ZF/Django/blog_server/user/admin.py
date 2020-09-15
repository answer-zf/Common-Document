from django.contrib import admin

# Register your models here.

from . import models


class UserProfileManager(admin.ModelAdmin):
    list_display = ['username', 'nickname', 'email',
                    'password', 'sign', 'info', 'avatar']


admin.site.register(models.UserProfile, UserProfileManager)
