from django.contrib import admin
from api.models.blog import Blog
from api.models.comment import Comment
from api.models.likes import CommentLike
from django.db import models

class BlogAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('title', 'created_at')
    search_fields = ('title', 'body')

class ReplyInline(admin.StackedInline):
    model = Comment
    fk_name = 'parent'
    extra = 0


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'blog', 'author', 'created_at')
    list_filter = ('blog', 'created_at')
    search_fields = ('body', 'author')
    inlines = [ReplyInline]

    def get_queryset(self, request):
        return super().get_queryset(request).filter(parent__isnull=True)


admin.site.register(Blog, BlogAdmin)
admin.site.register(CommentLike)
