# Create your views here.
from rest_framework import viewsets

# from .mixins import LikedMixin
from .models import Post, User
from .serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    # permission_classes = (AllowAny,)
    # authentication_classes = (TokenAuthentication, SessionAuthentication,)
    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ('isFan',)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
