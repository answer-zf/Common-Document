from django.contrib import admin

# Register your models here.

from . import models


class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'publisher',
                    'price', 'market_price']
    list_display_links = ['id', 'title']
    list_editable = ['market_price', 'publisher']


class AuthorManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'email']


class PublisherManager(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(models.Book, BookManager)
admin.site.register(models.Author, AuthorManager)
admin.site.register(models.Publisher, PublisherManager)
