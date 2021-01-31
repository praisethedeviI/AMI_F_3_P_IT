from rest_framework import serializers

from .models import Post
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'mail',
            'phone_number',
            'date',
            'password',
        )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id',
                  'username',
                  'body',
                  'created_at')
