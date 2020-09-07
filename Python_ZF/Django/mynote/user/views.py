from codecs import register
from django.shortcuts import render

# Create your views here.

from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from . import forms


def login(request):
    """
        用户登录
    """
    page_name = 'MyNote_Login'
    return render(request, 'login.html', locals())


def register(request):
    """
        用户注册
    """
    page_name = 'MyNote_Register'

    if request.method == 'GET':
        return render(request, 'register.html', locals())
    elif request.method == 'POST':
        myform = forms.RegForm(request.POST)
        if myform.is_valid():

            return HttpResponseRedirect('/')
        else:
            return HttpResponse('error')
