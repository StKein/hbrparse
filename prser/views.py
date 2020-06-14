from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view
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
    #queryset = get_object_or_404(Post, pk=pk)
"""
class PostViewSet(viewsets.ViewSet):
    def list(self, request):
        serializer = PostListSerializer(Post.objects.all(), many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)
"""