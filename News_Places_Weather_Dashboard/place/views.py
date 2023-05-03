from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Place
from .serializers import PostSerializer


class GetPlace(mixins.RetrieveModelMixin,
               GenericViewSet):
    queryset = Place.objects.all()
    serializer_class = PostSerializer

