from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserRegisterView, ClientViewSet
router = DefaultRouter()
router.register('users', UserViewSet)
router.register('clients', ClientViewSet)

from django.urls import path, include
urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', UserRegisterView.as_view(), name='register'),
]