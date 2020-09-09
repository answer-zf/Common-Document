from django.shortcuts import render

# Create your views here.

from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from . import forms
from . import models


def login(request):
    """
        用户登录
    """
    page_name = 'MyNote_Login'

    if request.method == 'GET':
        return render(request, 'login.html', locals())
    elif request.method == 'POST':

        myform = forms.LoginForm(request.POST)
        if myform.is_valid():

            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            try:
                user = models.User.objects.get(
                    username=username, password=password)

                request.session['userinfo'] = {
                    'username': user.username,
                    'id': user.id
                }

                return HttpResponseRedirect('/')

            except:
                return HttpResponse('error')

        else:
            return HttpResponse('error')


def logout(request):
    if 'userinfo' in request.session:
        del request.session['userinfo']

    return HttpResponseRedirect('/')


def register(request):
    """
        用户注册
    """
    page_name = 'MyNote_Register'

    if request.method == 'GET':
        return render(request, 'register.html', locals())
    elif request.method == 'POST':
        regform = forms.RegForm(request.POST)
        print(regform)
        if regform.is_valid():

            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            try:
                user = models.User.objects.create(
                    username=username, password=password)

                return HttpResponseRedirect('/user/login')

            except:
                return HttpResponse('error')

        else:
            return HttpResponse('valid error')
