from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.bookstore_homepage),
    url(r'^add$', views.bookstore_add),
    url(r'^list$', views.bookstore_list),
    url(r'^filter$', views.bookstore_filter),
    url(r'^mod/(\w+)$', views.bookstore_update),
    url(r'^del/(\w+)$', views.bookstore_delete),
]
