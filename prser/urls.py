""" API urls """
from django.conf.urls import include, url
from .views import PostList, PostDetail

urlpatterns = [
    url(r'^posts/$', PostList.as_view(), name='post-list'),
    url(r'^posts/(?P<pk>\d+)/$', PostDetail.as_view(), name='post-detail'),
]