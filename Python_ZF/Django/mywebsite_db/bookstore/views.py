from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    return render(request, 'bookstore/index.html')


def add_book(request):
    # /book/add?title='...’&pub='...'
    if request.method == 'GET':
        return render(request, 'bookstore/add.html')
    elif request.method == 'POST':
        title = request.POST.get('title', 'noname')
        publish = request.POST.get('pub', 'xxx')

        # 第一种创建
        from . import models
        models.Book.objects.create(title=title, pub=publish)

        return render(request, 'bookstore/index.html')
