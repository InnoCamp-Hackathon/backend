import requests
from django.conf import settings
from urllib.parse import quote_plus


def get_places(radius, lat, lon):
    res = requests.get(
        'https://maps.googleapis.com/maps/api/place/nearbysearch/json', params={
            'location': quote_plus(f'{lat},{lon}'),
            'type': 'park',
            'name': 'парк',
            'radius': radius,
            'language': 'ru',
            'key': settings.GOOGLEMAPS_API_KEY
        }).json()
    return res
