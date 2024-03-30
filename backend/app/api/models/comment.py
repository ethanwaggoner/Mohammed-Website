from django.db import models
from django.conf import settings


class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')
    author = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
