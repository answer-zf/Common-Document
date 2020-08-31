from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models

# Create your views here.


def mylogin(request):
    if request.method == 'GET':
        username = request.COOKIES.get('username', '')
        return render(request, 'userinfo/login.html', locals())
    elif request.method == 'POST':
        remember = request.POST.get('remember', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        resp = HttpResponse('login...')
        if remember:
            resp.set_cookie('username', username, 7*24*60*60)
        else:
            resp.delete_cookie('username')
        return resp


def myregister(request):
    if request.method == 'GET':
        return render(request, 'userinfo/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        # # 表单验证
        if not username:
            username_error = 'username not null'
            return render(request, 'userinfo/register.html', locals())
        if not password or not password2:
            password_error = 'password not null'
            return render(request, 'userinfo/register.html', locals())
        if password != password2:
            password_error = 'password must same!'
            return render(request, 'userinfo/register.html', locals())

        try:
            user = models.User.objects.create(
                username=username,
                password=password
            )
            return HttpResponse('register success!!')
        except:
            return HttpResponse('register Fail...')
