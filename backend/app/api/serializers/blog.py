from rest_framework import serializers
from api.models.blog import Blog
from api.serializers.comment import CommentSerializer


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'title', 'body', 'like_count', 'comments', 'comments_count', 'created_at']

    def get_like_count(self, obj):
        return obj.likes.count()

    def get_comments_count(self, obj):
        return obj.comments.count()