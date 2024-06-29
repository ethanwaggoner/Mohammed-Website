from django.contrib import admin
from api.models.blog import Blog
from api.models.comment import Comment
from api.models.likes import CommentLike
from django.db import models


class BlogAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('title', 'created_at')
    search_fields = ('title', 'body')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(CommentLike)
