from rest_framework import routers
from django.urls import path,include
from .apis import StudentViewSet, CustomStudentViewSet

router = routers.DefaultRouter()
router.register(r"old",StudentViewSet)
router.register(r"edited", CustomStudentViewSet, basename="Edited")

urlpatterns = [
    path("",include(router.urls)),
]
