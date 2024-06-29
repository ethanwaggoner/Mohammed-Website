from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models.blog import Blog
from api.models.comment import Comment
from api.serializers.blog import BlogSerializer
from api.serializers.comment import CommentSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['tags__name']
    search_fields = ['title', 'body']
    ordering_fields = ['created_at', 'title']

    def get_queryset(self):
        queryset = Blog.objects.prefetch_related('comments', 'tags').all()
        tags = self.request.query_params.get('tags')
        if tags:
            tag_list = tags.split(',')
            queryset = queryset.filter(tags__name__in=tag_list).distinct()
        return queryset

    @action(detail=True, methods=['post'])
    def add_comment(self, request, slug=None):
        blog = self.get_object()
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(blog=blog)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
