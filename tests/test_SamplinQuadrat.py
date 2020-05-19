import unittest
from geoambiental import Point
import numpy as np

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
        self.assertEqual(self.cuadrante.lat, 59)

    def test_x_is_a_property(self):
        """
        """
        self.assertAlmostEqual(self.cuadrante.x, np.array(399086.97330437))

    def test_y_is_a_property(self):
        """
        """
        self.assertAlmostEqual(self.cuadrante.y, np.array(2765319.94402007))

    def test_utm_zone_is_a_property(self):
        """
        """
        self.assertTrue(np.array_equal(self.cuadrante.utm_zone, np.array(['11', 'R'], dtype='<U21')))


if __name__ == '__main__':
    unittest.main()
