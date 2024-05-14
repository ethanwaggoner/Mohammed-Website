from django.contrib import admin
from api.models.blog import Blog
from api.models.comment import Comment
from api.models.likes import CommentLike

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(CommentLike)
