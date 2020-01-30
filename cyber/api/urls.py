from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UsuarioViewSet


router = routers.DefaultRouter()
router.register('users',UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
