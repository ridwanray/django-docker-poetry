from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    published = models.BooleanField(default=True)
    extra_info = models.CharField(max_length=50,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


