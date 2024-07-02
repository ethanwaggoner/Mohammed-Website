from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.models.blog import Blog
from api.models.comment import Comment
from api.serializers.comment import CommentSerializer
import logging
from api.services.spamprotection import is_spam

logger = logging.getLogger(__name__)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        blog_slug = request.data.get('blog_slug')
        if not blog_slug:
            return Response({'detail': 'Blog slug is required.'}, status=status.HTTP_400_BAD_REQUEST)

        blog = get_object_or_404(Blog, slug=blog_slug)

        parent_id = request.data.get('parent_id')
        if parent_id:
            parent = get_object_or_404(Comment, id=parent_id, blog=blog)
        else:
            parent = None

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(blog=blog, parent=parent)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
