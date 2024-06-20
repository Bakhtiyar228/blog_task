from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .token_views import MyTokenObtainPairView, MyTokenRefreshView
from .views import PostViewSet, CommentViewSet, register_user

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register_user, name='register_user'),
]
