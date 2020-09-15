from django.conf.urls import url

from . import views

# 主模块路由：/v1/users

urlpatterns = [
    url(r'^$', views.users, name='users'),
    url(r'^/(?P<username>[\w]{6,11})$', views.users, name='user')
]
