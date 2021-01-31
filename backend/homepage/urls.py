from rest_framework import routers

from .views import PostViewSet, UserViewSet

# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register(r'notes', PostViewSet)
router.register(r'users', UserViewSet)
# URLs настраиваются автоматически роутером
urlpatterns = router.urls
