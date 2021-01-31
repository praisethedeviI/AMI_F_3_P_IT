from rest_framework import serializers

from .models import Post
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'phone_number',
            'username',
            'first_name',
            'last_name',
            'date', 'date_joined'
        )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id',
                  'username',
                  'body',
                  'created_at')
