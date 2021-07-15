from django.db import models

class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True, default="")
    content = models.TextField()

    class Meta:
        ordering = ['created']


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255, blank=True, default='admin')
    content = models.TextField()

    class Meta:
        ordering = ['created']