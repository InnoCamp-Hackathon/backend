from rest_framework import generics
from rest_framework.exceptions import ParseError

from .models import Place
from .serializers import PlaceSerializer
from .services.point import Point


class PlacesList(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def filter_queryset(self, queryset):
        if any(param not in self.request.query_params for param in ['radius', 'lat', 'lon']):
            raise ParseError('Missed required parameter')
        try:
            point = Point(float(self.request.query_params['lat']), float(self.request.query_params['lon']))
            radius = int(self.request.query_params['radius'])
        except ValueError:
            raise ParseError('Parameters wrong type')
        filtered_places_ids = set(place.id for place in Place.objects.all() if place.distance(point) <= radius)
        return queryset.filter(id__in=filtered_places_ids)
