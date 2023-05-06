from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_router = SimpleRouter()
v1_router.register("posts", PostViewSet)
v1_router.register("groups", GroupViewSet)
v1_router.register(
    r"posts/(?P<post_id>[^/.]+)/comments",
    CommentViewSet,
    basename="comments",
)
v1_router.register("follow", FollowViewSet)

urlpatterns = [
    path("v1/", include(v1_router.urls)),
    path("v1/jwt/create/", TokenObtainPairView.as_view(), name="jwt-create"),
    path("v1/jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("v1/jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
]
