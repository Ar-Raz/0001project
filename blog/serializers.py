from rest_framework import serializers

from .models import Post, Comment

from users.serializers import UserSerializer
from jalali_date import date2jalali


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value

#POSTS
class PostSerializer(serializers.ModelSerializer):
    categories = StringSerializer(many=True)
    author = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'short_description',
            'content',
            'timestamp',
            'thumbnail',
            'categories',
            'featured',
            'active_post',
            'slug',
            'author',
            'avg_read',
            'date',
        )
        read_only_fields = ['pk', 'featured']

    def get_author(self, obj):
        return UserSerializer(obj.author).data

    def get_date(self, obj):
        return str(date2jalali(obj.timestamp))

#COMMENTS)

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    post = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'id',
            'timestamp',
            'content',
            'user',
            'post',
            'username'
        )
        read_only_fields = ['pk', 'user']

    def get_user(self, obj):
        return UserSerializer(obj.user).data

    def get_post(self, obj):
        return PostSerializer(obj.post).data



class PostDetailSerializer(serializers.ModelSerializer):
    categories = StringSerializer(many=True)
    author = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'short_description',
            'content',
            'timestamp',
            'thumbnail',
            'categories',
            'featured',
            'active_post',
            'slug',
            'author',
            'comments',
            'avg_read',
            'date',

        )

    def get_author(self, obj):
        return UserSerializer(obj.author).data

    def get_comments(self, obj):
        return CommentSerializer(obj.get_comment, many=True).data

    def get_date(self, obj):
        return str(date2jalali(obj.timestamp))


class CommentsUndetailedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'id',
            'content',
            'user',
            'timestamp',
            'post'
        )
