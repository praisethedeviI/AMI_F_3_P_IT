from rest_framework import routers

from .views import PostViewSet, UserViewSet

# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register(r'notes', PostViewSet)
router.register(r'users', UserViewSet)
# URLs настраиваются автоматически роутером
urlpatterns = router.urls

# from django.contrib.contenttypes.models import ContentType
#  from likes.models import Like
#  from tweets.models import Tweet
#  from django.contrib.auth import get_user_model
#  User = get_user_model()
#  user = User.objects.create_user(username='testuser', password='testuser')
#  tweet = Tweet.objects.create(body='People are space puppets')
#  tweet_model_type = ContentType.objects.get_for_model(tweet)
#  Like.objects.create(content_type=tweet_model_type, object_id=tweet.id, user=user)
#  Like.objects.count()
# Like.objects.first().content_object
#  tweet.total_likes
