from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from api.models.blog import Blog
from api.serializers.blog import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
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