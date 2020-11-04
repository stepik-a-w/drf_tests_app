from rest_framework.routers import SimpleRouter

from .views import BookViewSet

router = SimpleRouter()
router.register('', BookViewSet)

urlpatterns = router.urls
