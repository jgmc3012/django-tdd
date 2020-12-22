from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MovieViewSet

router = DefaultRouter()

router.register(r"", MovieViewSet)

urlpatterns = [
    path("api/movies/", include(router.urls)),
]
