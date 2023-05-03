from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = SimpleRouter()
router.register("posts", PostViewSet)
router.register("groups", GroupViewSet)
router.register(r"posts/(?P<post_id>[^/.]+)/comments", CommentViewSet)
router.register("follow", FollowViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/", include("djoser.urls.jwt")),
]
