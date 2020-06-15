""" API views """
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import PostListSerializer, PostDetailSerializer
from .models import Post


class PostList(generics.ListAPIView):
    """ API resource representing a list of posts """
    model = Post
    serializer_class = PostListSerializer
    queryset = Post.objects.all()

class PostDetail(generics.RetrieveAPIView):
    """ API resource representing a single post """
    model = Post
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()