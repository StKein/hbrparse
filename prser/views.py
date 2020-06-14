from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PostListSerializer, PostDetailSerializer
from .models import Post

class PostViewSet(viewsets.ViewSet):
    def list(self, request):
        serializer = PostListSerializer(Post.objects.all(), many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)