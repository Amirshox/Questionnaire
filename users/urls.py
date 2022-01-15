# Django
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

# Project
from .views import UserViewSet

router = DefaultRouter()

router.register('user', UserViewSet, 'user')

urlpatterns = [
    re_path(r'^login/?$', ObtainAuthToken.as_view(), name='login'),
    path('', include(router.urls)),
]
