from django.db import router
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet

router = DefaultRouter()

router.register( 'user', UserViewSet, basename='users' )

urlpatterns = router.urls