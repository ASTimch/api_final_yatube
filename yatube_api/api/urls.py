from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import GroupViewSet, PostViewSet

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]
