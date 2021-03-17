from rest_framework import serializers

from .models import Post


class SimplePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('text',)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
