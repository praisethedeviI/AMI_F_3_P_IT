from django.contrib.auth import get_user_model
from rest_framework import serializers

from . import services as likes_services
from .models import Post, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'phone_number',
            'username',
            'password',
            'first_name',
            'last_name',
            'date',
            'date_joined'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class PostSerializer(serializers.ModelSerializer):
    User2 = get_user_model()

    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = {'user_id': {'read_only': True}, 'username': {'read_only': True}}

        def get_is_fan(self, obj) -> bool:
            """Check if a `request.user` has liked this tweet (`obj`).
            """
            user = self.context.get('request').user
            return likes_services.is_fan(obj, user)

    def create(self, validated_data):
        user = self.context.get('request').user
        post = Post(
            user_id=user,
            username=user.username,
            body=validated_data['body'],
        )
        post.save()
        return post



class FanSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'username',
            'full_name',
        )

    @staticmethod
    def get_full_name(obj):
        return obj.get_full_name()
