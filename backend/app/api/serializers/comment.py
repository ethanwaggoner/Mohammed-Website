from rest_framework import serializers
from api.models.comment import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'body', 'author', 'created_at']
        read_only_fields = ['author', 'created_at']