from rest_framework import routers

from .views import PostViewSet

# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register(r'notes', PostViewSet)
# URLs настраиваются автоматически роутером
urlpatterns = router.urls