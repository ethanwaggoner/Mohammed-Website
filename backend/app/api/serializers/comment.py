from rest_framework import serializers
from api.models.comment import Comment

class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class CommentSerializer(serializers.ModelSerializer):
    replies = RecursiveField(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'body', 'author', 'created_at', 'replies', 'parent', 'is_admin_reply']
        read_only_fields = ['created_at', 'is_admin_reply']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['parent_id'] = instance.parent_id
        return representation
