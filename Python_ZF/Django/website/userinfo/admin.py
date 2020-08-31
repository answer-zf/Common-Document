from django.contrib import admin

# Register your models here.
from . import models


class BookManager(admin.ModelAdmin):
    list_display = ['username', 'password']


admin.site.register(models.User, BookManager)
