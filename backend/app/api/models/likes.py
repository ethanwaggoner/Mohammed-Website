from django.db import models


class CommentLike(models.Model):
    ip_address = models.GenericIPAddressField()
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f"User from IP {self.ip_address} likes Comment {self.comment}"

    class Meta:
        unique_together = ('ip_address', 'comment')