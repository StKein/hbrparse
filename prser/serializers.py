""" REST serializers """
from rest_framework import serializers
from .models import Post

""" Serializer for posts list resource """
class PostListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'annonce', 'inner_link')

""" Serializer for one post resource """
class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'link', 'text')