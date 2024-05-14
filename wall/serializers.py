from rest_framework import serializers

from profiles.models import UserProfile
from .models import Post, CommentPostModel, LikePostModel


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentPostModel
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikePostModel
        fields = '__all__'
