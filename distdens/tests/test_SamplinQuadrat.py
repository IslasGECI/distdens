import unittest

from ..models import SamplingQuadrat


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


if __name__ == '__main__':
    unittest.main()
