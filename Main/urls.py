from django.conf.urls import url

from .views import (
    index,
    post_create,
    post_detail,
    post_list
)

urlpatterns = [
    url(r'^home/$',index,name='index'),
    url(r'^$',post_list,name='list'),
    url(r'^create/$',post_create,name='create'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
]



