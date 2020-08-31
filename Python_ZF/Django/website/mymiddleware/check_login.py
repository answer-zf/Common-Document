from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


class MyMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print('process request  callback')
        # return None
        return HttpResponse('intercept .............')
