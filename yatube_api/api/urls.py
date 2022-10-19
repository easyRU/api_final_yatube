from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet


router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('groups', GroupViewSet, basename='groups')
router_v1.register('follow', FollowViewSet, basename='follow')
router_v1.register(r'posts/(?P<post_pk>\d+)/comments',
                CommentViewSet, basename='comments')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]