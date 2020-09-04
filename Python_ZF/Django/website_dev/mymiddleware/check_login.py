from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

import re


class MyMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print('process request  callback')
        # return None
        if re.match(r'^/bookstore', request.path_info) \
                and ('userinfo' not in request.session):
            return HttpResponseRedirect('/userinfo/login')
        return None

# 反扒


class VisitLimit(MiddlewareMixin):
    """
        限制一个 IP 访问 /user/login 的次数不能超过 5次
    """

    visit_times = {}  # 客户端IP地址访问次数

    def process_request(self, request):
        ip_address = request.META['REMOTE_ADDR']
        if not re.match('^/text', request.path_info):
            return
        times = self.visit_times.get(ip_address, 0)
        print("IP", ip_address, "___ visit ", times,
              "times. for ", request.path_info)
        self.visit_times[ip_address] = times+1
        if times < 5:
            return
        return HttpResponse('Forbidden...')
