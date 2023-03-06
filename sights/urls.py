from rest_framework.routers import SimpleRouter

from .views import SightsViewSet

router = SimpleRouter(trailing_slash=False)
router.register('', SightsViewSet, basename='sight')

urlpatterns = router.urls
