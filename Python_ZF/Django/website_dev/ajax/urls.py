from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^load/$', views.load),
    url(r'^server/$', views.server),
    url(r'^get/$', views.get_views),
    url(r'^get_server/$', views.get_server),
]
