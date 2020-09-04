import email
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

from django.conf import settings  # 导入当前项目的 settings 模块
import os


def homepage(request):
    return render(request, 'index.html', locals())


def text(request):
    return render(request, 'index.html', locals())


def on_upload(request):
    if request.method == 'GET':
        return render(request, 'upload.html', locals())
    elif request.method == 'POST':
        myfile = request.FILES['myfile']
        with open(os.path.join(settings.MEDIA_DIR, myfile.name), 'wb') as fd:
            file_content = myfile.file.read()
            fd.write(file_content)
        return HttpResponse('ok')
