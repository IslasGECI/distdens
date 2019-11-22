import unittest
import pandas as pd
from distdens.io import QuadratTableReader

data = {'Especie': ['Synthliboramphus hypoleucus','Synthliboramphus hypoleucus','Especie2'], \
'Sitio_o_colonia': ['Morro Prieto','Sitio2','Morro Prieto'], \
'Area_del_cuadrante': [4,4,4], \
'Madrigueras_con_actividad_aparente': [0,1,2], \
'Este': [374448,374458,374542], \
'Norte': [3198223,3198229,3198266],
'Zona_utm':['11R','11R','11R']}

datos=pd.DataFrame(data)

filtro = {"Sitio_o_colonia": "Morro Prieto",
          "Especie": "Synthliboramphus hypoleucus"}

class TestQuadratTableReader(unittest.TestCase):

    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        self.cuadrantes = QuadratTableReader.read(datos, filtro)

    def test_get_density(self):
        """
        Verifica que la densidad de calcule de manera correcta
        """
        self.assertTrue(type(self.cuadrantes).__name__ == 'ndarray')


if __name__ == '__main__':
    unittest.main()