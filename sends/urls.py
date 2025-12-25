from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SendViewSet

router = DefaultRouter()
router.register(r'', SendViewSet, basename='send')

urlpatterns = [
    path('', include(router.urls)),
]

