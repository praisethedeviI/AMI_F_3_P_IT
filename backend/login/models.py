from django.db import models


# Create your models here.

class Post(models.Model):
    # image_user = models.ImageField()
    username = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
