from django.contrib.auth import get_user_model
from rest_framework import serializers

from . import services as likes_services
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
                  'total_likes',
                  'created_at')

        def get_is_fan(self, obj) -> bool:
            """Check if a `request.user` has liked this tweet (`obj`).
            """
            user = self.context.get('request').user
            return likes_services.is_fan(obj, user)


User2 = get_user_model()


class FanSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User2
        fields = (
            'username',
            'full_name',
        )

    @staticmethod
    def get_full_name(obj):
        return obj.get_full_name()
