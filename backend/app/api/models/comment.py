from django.db import models
from django.conf import settings


class Comment(models.Model):
    body = models.TextField()
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.blog}"
