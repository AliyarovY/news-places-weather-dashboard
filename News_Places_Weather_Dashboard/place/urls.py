from django.urls import include, path
from rest_framework import routers

from .views import GetPlace

router = routers.DefaultRouter()
router.register(r'place', GetPlace)

urlpatterns = [
    path('', include(router.urls)),
]
