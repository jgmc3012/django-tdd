from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from .models import Movie
from .serializers import MovieSerializer


class MovieViewSet(mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
