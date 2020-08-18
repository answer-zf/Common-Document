from django.http import HttpResponse


def homepage(request):
    return HttpResponse("this .is .homepage...")


def pageyear(request, y):
    return HttpResponse("this.is.yearpage.%s" % y)


def birthday(request, y, m, d):
    return HttpResponse('birthday is %s-%s-%s' % (y, m, d))


def person(request, name, age):
    return HttpResponse("this is %s, %s" % (name, age))


def add(request, first, last):
    return HttpResponse("%s + %s = %d" % (first, last, int(first) + int(last)))
