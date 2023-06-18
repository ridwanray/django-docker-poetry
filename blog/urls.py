from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import BlogViewSet

app_name = "blog"

router = DefaultRouter()
router.register("", BlogViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
