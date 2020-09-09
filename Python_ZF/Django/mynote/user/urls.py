from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^reg/$', views.register),
    url(r'^logout/$', views.logout),
]
