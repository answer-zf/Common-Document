from django.contrib.auth.models import AbstractUser
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import models
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def mylogin2(request):
    if request.method == 'GET':
        return render(request, 'user/login.html', locals())
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        # try:
        #     user = models.User.objects.get(username=username)  # 缺少 is_actice=True
        #     if user.check_password(password):
        #         return HttpResponse('login success')
        #     else:
        #         return HttpResponse('password error..')

        # except:
        #     return HttpResponse('user not exist..')

        # 简化认证
        user = authenticate(username=username, password=password)
        if user is not None:
            # 登录
            login(request, user)
            return HttpResponse('login success')
        else:
            return HttpResponse('login fail')


def mylogout2(request):
    logout(request)
    return HttpResponse('logout')


def myregister2(request):
    if request.method == 'GET':
        return render(request, 'user/register.html', locals())
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        # ...

        try:
            user = models.User.objects.create_superuser(
                username=username,
                password=password,
                email='657829956@qq.com'
            )
            user.save()
            return HttpResponse('reg success')
        except:
            return HttpResponse('reg fail')
