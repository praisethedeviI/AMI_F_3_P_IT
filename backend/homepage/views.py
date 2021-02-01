# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
# from .mixins import LikedMixin
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import permissions

from .permissions import *
from .mixins import LikedMixin
from .models import Post, User
from .serializers import PostSerializer, UserSerializer


class PostViewSet(LikedMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, )

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes = (WriteOnly|permissions.IsAdminUser, )