import requests
from django.conf import settings


def is_weather_normal(place_object) -> bool:
    lat = place_object.lat
    lon = place_object.lon
    res = requests.get('api.openweathermap.org/data/2.5', params={
        'appid': settings.OPENWEATHERMAP_API_KEY,
        'lat': lat,
        'lon': lon
    }).json()
    if res['weather']['main'] == 'Clear':
        return True
    else:
        return False
