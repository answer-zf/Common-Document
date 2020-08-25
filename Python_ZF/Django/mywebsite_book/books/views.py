from django.shortcuts import render

# Create your views here.
from . import models


def homepage(request):
    return render(request, 'index.html')


def add_book(request):
    if request.method == 'GET':
        return render(request, 'add_book.html')
    elif request.method == 'POST':
        title = request.POST.get('title', '')
        pub = request.POST.get('pub', '')
        price = request.POST.get('price', '0')
        market_price = request.POST.get('market_price', '')

        # 1.
        # models.Book.objects.create(
        #     title=title,
        #     pub=pub,
        #     price=price,
        #     market_price=market_price,
        # )

        abook = models.Book()
        abook.title = title
        abook.pub = pub
        abook.price = price
        abook.market_price = market_price
        abook.save()

        return render(request, 'index.html')


def book_list(request):
    books = models.Book.objects.all()
    return render(request, 'book_list.html', locals())
