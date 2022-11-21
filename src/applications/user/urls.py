from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("profile", views.UserProfileViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("login/", views.UserLoginApiView.as_view()),
]
