from django.db import models
from django.conf import settings


class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']