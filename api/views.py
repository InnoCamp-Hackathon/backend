from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from .services.get_places import get_places
from .services.point import Point
from .services.check_weather import is_weather_normal


class PlacesList(APIView):
    def get(self, request: Request) -> Response:
        if any(param not in self.request.query_params for param in ['radius', 'lat', 'lon']):
            raise ParseError('Missed required parameter')
        try:
            point = Point(float(self.request.query_params['lat']), float(self.request.query_params['lon']))
            radius = int(self.request.query_params['radius'])
        except ValueError:
            raise ParseError('Parameters wrong type')
        places = get_places(radius, point.lat, point.lon)
        places = list(filter(
            lambda place: is_weather_normal(
                Point(
                    place['geometry']['location']['lat'],
                    place['geometry']['location']['lng']
                )
            ),
            places
        ))
        return Response(places)
