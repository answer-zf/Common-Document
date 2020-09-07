from codecs import register
from django.shortcuts import render

# Create your views here.

from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def login(request):
    page_name = 'MyNote_Login'
    return render(request, 'login.html', locals())


def register(request):
    page_name = 'MyNote_Register'
    if request.method == 'GET':
        return render(request, 'register.html', locals())
    elif request.method == 'POST':
        pass
