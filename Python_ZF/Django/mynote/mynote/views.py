from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import render


def homepage(request):
    return render(request, 'index.html')
