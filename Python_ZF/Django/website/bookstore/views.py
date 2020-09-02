from django.db.models import F
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.paginator import Paginator

# Create your views here.
from . import models


def bookstore_homepage(request):

    return render(request, 'bookstore_homepage.html')


def bookstore_add(request):

    if request.method == 'GET':
        return render(request, 'bookstore_add.html')
    elif request.method == 'POST':
        title = request.POST.get('title', '')
        pub = request.POST.get('pub', '')
        price = request.POST.get('price', '0')
        market_price = request.POST.get('market_price', '')

        abook = models.Book()
        abook.title = title
        abook.pub = pub
        abook.price = price
        abook.market_price = market_price
        abook.save()

        return HttpResponseRedirect('/bookstore/list')


def bookstore_list(request):

    books = models.Book.objects.all()
    return render(request, 'bookstore_list.html', locals())


def bookstore_filter(request):

    books = models.Book.objects.filter(price__gte=50)
    return render(request, 'bookstore_list.html', locals())


def bookstore_update(request, id):

    if request.method == 'GET':
        abook = models.Book.objects.get(id=id)
        return render(request, 'bookstore_update.html', locals())
    elif request.method == 'POST':
        abook = models.Book.objects.get(id=id)
        now_price = request.POST.get('market_price', 9999)
        abook.market_price = float(now_price)
        abook.save()
        return HttpResponseRedirect('/bookstore/list')


def bookstore_delete(request, id):

    abook = models.Book.objects.get(id=id)
    abook.delete()
    return HttpResponseRedirect('/bookstore/list')


def bookstore_book(request):
    books = models.Book.objects.all()
    paginator = Paginator(books, 5)
    p_count = paginator.count
    p_num = paginator.num_pages
    p_range = paginator.page_range
    p_per = paginator.per_page

    cur_page = request.GET.get('page', 1)
    page = paginator.page(cur_page)  # 当前页所有信息
    return render(request, 'bookstore_book.html', locals())
