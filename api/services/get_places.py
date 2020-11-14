import requests
from django.conf import settings
from urllib.parse import quote_plus
from typing import Dict


def get_places(radius: int, lat: float, lon: float) -> Dict:
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
