import requests
from django.conf import settings
from .point import Point


def is_weather_normal(place_object: Point) -> bool:
    lat = place_object.lat
    lon = place_object.lon
    res = requests.get('http://api.openweathermap.org/data/2.5/weather', params={
        'appid': settings.OPENWEATHERMAP_API_KEY,
        'lat': lat,
        'lon': lon
    })
    res_json = res.json()
    if 200 <= res.status_code < 300 and res_json['weather'][0]['main'] in {'Clear', 'Clouds'}:
        return True
    else:
        return False

