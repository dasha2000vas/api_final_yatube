from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowList, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(
    r'posts/(?P<post_pk>\d+)/comments', CommentViewSet,
    basename='comments'
)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/follow/', FollowList.as_view()),
]
