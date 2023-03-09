from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    writer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="article"
    )

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="article/", null=False)
    content = models.TextField(max_length=500, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
