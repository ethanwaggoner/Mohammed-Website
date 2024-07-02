from django.db import models

class Comment(models.Model):
    body = models.TextField()
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    is_admin_reply = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.author} on {self.blog}"
