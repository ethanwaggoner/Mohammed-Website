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
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            try:
                author_name = request.data.get('author_name')
                comment_body = request.data.get('body')
                if is_spam(author_name, comment_body):
                    return Response({'detail': 'Comment contains spam.'}, status=status.HTTP_400_BAD_REQUEST)

                serializer.save(blog=blog)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                logger.error(f"Error in creating a comment: {e}", exc_info=True)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            logger.warning(f"Validation errors in creating a comment: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)