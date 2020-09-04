
from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField('名称', max_length=50, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):

    name = models.CharField('姓名', unique=True, db_index=True, max_length=20)
    age = models.IntegerField('年龄', default='1')
    email = models.EmailField('邮箱', null=True)

    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(
        verbose_name='书名', max_length=50, default='', unique=True)
    price = models.DecimalField(
        '定价', max_digits=7, decimal_places=2, default=0)
    market_price = models.DecimalField(
        '零售价', max_digits=7, decimal_places=2, default=0)
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, null=True)

    authors = models.ManyToManyField(Author, null=True)

    def __str__(self):
        return self.title
