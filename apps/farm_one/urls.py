from django.urls import include, path

from .views import *
from rest_framework.routers import DefaultRouter

from .views import FarmOneViewSet

app_name = "farm_one"
router = DefaultRouter()
router.register(r"", FarmOneViewSet, basename="farm_one")
urlpatterns = [
    path("", include(router.urls)),
    # path("students/", StudentsViewSet.as_view(), name="students"),
]