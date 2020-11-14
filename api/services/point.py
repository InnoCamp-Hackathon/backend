from dataclasses import dataclass


@dataclass(order=False)
class Point:
    """Class to represent point on the Earth"""
    lat: float
    lon: float
