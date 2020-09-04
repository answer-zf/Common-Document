from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField('username', max_length=30, unique=True)
    password = models.CharField('password', max_length=30)

    def __str__(self):
        return 'user' + self.username
