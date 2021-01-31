from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255)
    mail = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=127)
    date_joined = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    # image_user = models.ImageField()
    username = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
