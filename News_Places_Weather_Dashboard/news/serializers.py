from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import News


class NewsSerializer(ModelSerializer):
    author = serializers.CurrentUserDefault()

    class Meta:
        model = News
        fields = [
            'title',
            'main_image',
            'preview_image',
            'text',
            'pub_date',
            'author'
        ]
