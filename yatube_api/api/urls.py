from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, FollowViewSet, GropViewSet, PostViewSet

v1_router = SimpleRouter()
v1_router.register(
    'posts/(?P<post_id>\\d+)/comments',
    CommentViewSet,
    basename='comments'
)
v1_router.register('follow', FollowViewSet, basename='follows')
v1_router.register('groups', GropViewSet, basename='groups')
v1_router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
