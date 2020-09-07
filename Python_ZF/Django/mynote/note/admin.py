from django.contrib import admin

# Register your models here.
from . import models


class NoteManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'create_time', 'mod_time']


admin.site.register(models.Note, NoteManager)
