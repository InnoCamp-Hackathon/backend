from django.db import models
from django.db.models import fields as fl
from math import radians, sin, cos, atan2, sqrt


class Place(models.Model):
    lat = fl.FloatField()
    lon = fl.FloatField()
    title = fl.CharField(max_length=64)

    def distance(self, point) -> float:
        r_lat1, r_lat2 = radians(self.lat), radians(point.lat)
        r_lon1, r_lon2 = radians(self.lon), radians(point.lon)
        delta_lon = r_lat1 - r_lat2
        delta_lat = r_lon1 - r_lon2
        a = sin(delta_lat / 2) ** 2 + cos(r_lat1) * cos(r_lat2) * sin(delta_lon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        r = 6373000.  # Earth radius in meters
        res = c * r
        return res
