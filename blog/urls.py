from django.conf.urls import url
from .views import *

from . import views

 
urlpatterns = [
    url(r'^$', post_list, name="blog"),
    url(r'^(?P<id>\d+)/$', post_detail),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^(?P<id>\d+)/edit$', views.edit_post),
]