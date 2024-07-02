from django.contrib import admin
from api.models.comment import Comment

class ReplyInline(admin.StackedInline):
    model = Comment
    fk_name = 'parent'
    extra = 0

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'blog', 'author', 'created_at', 'is_admin_reply')
    list_filter = ('blog', 'created_at')
    search_fields = ('body', 'author')
    inlines = [ReplyInline]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.is_admin_reply = True
        super().save_model(request, obj, form, change)
