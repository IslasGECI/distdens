import unittest
from geoambiental import Point

from distdens.models import SamplingQuadrat


class TestGeoCircle(unittest.TestCase):

    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        self.cuadrante = SamplingQuadrat(25, -118, 25, 50)

    def test_get_density(self):
        """
        Verifica que la densidad de calcule de manera correcta
        """
        self.assertTrue(self.cuadrante.get_density() == 50/25)

    def test_type_Point(self):
        """
        Verifica que la densidad de calcule de manera correcta
        """
        self.assertTrue(type(self.cuadrante._point).__name__ == 'Point')

    def test_lat_as_property(self):
        """
        Verifica que la densidad de calcule de manera correcta
        """
        self.cuadrante._point = Point(59, 30)
        self.assertTrue(self.cuadrante.lat == 59)


if __name__ == '__main__':
    unittest.main()
