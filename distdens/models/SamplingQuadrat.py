from geoambiental import Point


class SamplingQuadrat:
    def __init__(self, lat: float, lon: float, area: float, count: int):
        self._area = area
        self._count = count
        self._point = Point(lat, lon)

    def get_density(self):
        return self.count/self.area

    @property
    def area(self):
        return self._area

    @property
    def count(self):
        return self._count

    @property
    def lat(self):
        return self._point.lat

    @property
    def lon(self):
        return self._point.lon

    @property
    def y(self):
        return self._point.y

    @property
    def x(self):
        return self._point.x

    @property
    def utm_zone(self):
        return self._point.utm_zone
