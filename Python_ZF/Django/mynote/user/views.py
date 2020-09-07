from django.shortcuts import render

# Create your views here.

from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def login(request):
    page_name = 'MyNote_Login'
    request.session['userinfo'] = {
        'id': 1,
        'username': 'zf'
    }
    return render(request, 'login.html', locals())
