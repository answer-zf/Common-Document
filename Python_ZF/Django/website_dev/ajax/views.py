from django.http import HttpResponse
from django.shortcuts import render

import json

from requests.api import request

# Create your views here.


def load(request):
    return render(request, 'load.html')


def server(request):
    uname = request.POST.get('uname')
    uage = request.POST.get('uage')
    return render(request, 'server.html', locals())


def get_views(request):
    return render(request, 'get.html')


def get_server(request):
    dic = {
        'uname': 'zf',
        'uage': 16,
    }
    jsonStr = json.dumps(dic)
    return HttpResponse(jsonStr)
