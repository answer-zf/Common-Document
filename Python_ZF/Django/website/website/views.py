from django.shortcuts import render


def homepage(request):
    return render(request, 'index.html', locals())


def text(request):
    return render(request, 'index.html', locals())
