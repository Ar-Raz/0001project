from rest_framework import serializers

from .models import MetaTagsBase

class MetaTagSerializer(serializers.Serializer):
    meta_keyword = serializers.CharField()
    meta_description = serializers.CharField()
    meta_copytight = serializers.CharField()
    meta_author = serializers.CharField()
