from rest_framework import serializers
from api.models.comment import Comment
from api.models.blog import Blog


class CommentSerializer(serializers.ModelSerializer):
    blog = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'body', 'blog', 'created_at']
