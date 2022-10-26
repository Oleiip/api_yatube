from rest_framework.routers import DefaultRouter

from django.urls import include, path
from rest_framework.authtoken import views
from api.views import PostViewSet, GroupViewSet, CommentViewSet


v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupViewSet)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('api/v1/', include(v1_router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]