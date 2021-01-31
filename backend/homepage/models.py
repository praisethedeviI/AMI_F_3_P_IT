# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.fields import GenericRelation
# from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255)
    mail = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    date = models.DateTimeField()
    password = models.CharField(max_length=127)
    date_joined = models.DateTimeField(auto_now_add=True)


# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveSmallIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')


class Post(models.Model):
    username = models.CharField(max_length=255)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # likes = GenericRelation(Like)

    # @property
    # def total_likes(self):
    #     return self.likes.count()
