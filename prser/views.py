from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import PostListSerializer, PostDetailSerializer
from .models import Post


class PostList(generics.ListAPIView):
    """
        API endpoint that represents a list of Posts.
    """
    model = Post
    serializer_class = PostListSerializer
    queryset = Post.objects.all()

class PostDetail(generics.RetrieveAPIView):
    """
        API endpoint that represents a single Post.
    """
    model = Post
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()