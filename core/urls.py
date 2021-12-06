"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import Login, Logout, Register, pago

urlpatterns = [
    path( 'admin/', admin.site.urls ),
    path( 'api-auth/', include( 'rest_framework.urls' ) ),
    path( 'user/login/', Login.as_view(), name = 'login' ),
    path( 'user/logout/', Logout.as_view(), name = 'logout' ),
    path( 'user/register/', Register.as_view(), name = 'register' ),
    path( 'user/', include( 'users.routers' ) ),
    path( 'rooms/', include( 'rooms.routers' ) ),
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name = 'token_obtain_pair'
    ),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name = 'token_refresh'
    ),
    path( 'user/pago/', pago, name = 'pago' ),
    
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root = settings.STATIC_ROOT
    )
