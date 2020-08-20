from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render


# def page_template(request):
#     return render(request, 'page.html')

def page_template(request):
    t = loader.get_template('page.html')  # 加载模板
    html = t.render({
        'name': 'zf',
        'age': 60,
        'fav': ['zzzz', 'ccc', 'ddd', 'eee']
    })  # 渲染成字符串
    return HttpResponse(html)


def page4(request):
    string = 'this is page4'
    a = '<span>zzzzzzzzzzz</span>'
    b = 200
    return render(request, 'page4.html', locals())
