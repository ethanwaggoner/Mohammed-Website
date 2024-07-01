from django.db import models
from django.conf import settings
from django.utils.text import slugify
import itertools
from taggit.managers import TaggableManager
from django_ckeditor_5.fields import CKEditor5Field

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    body = CKEditor5Field('Text', config_name='extends')
    image = models.ImageField(upload_to='images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_blogs', blank=True)
    tags = TaggableManager(blank=True)
    restricted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            for i in itertools.count(1):
                if not Blog.objects.filter(slug=slug).exists():
                    break
                slug = f"{base_slug}-{i}"
            self.slug = slug
        super().save(*args, **kwargs)
