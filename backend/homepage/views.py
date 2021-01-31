# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny

from .mixins import LikedMixin
from .models import Post, User
from .serializers import PostSerializer, UserSerializer


class PostViewSet(LikedMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication, SessionAuthentication,)
    filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ('isFan',)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
