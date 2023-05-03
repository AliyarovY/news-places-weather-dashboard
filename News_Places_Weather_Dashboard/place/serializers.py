from rest_framework import serializers

from .models import Place


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['name', 'latitude', 'longitude', 'rating']
