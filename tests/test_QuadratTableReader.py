import unittest
import pandas as pd
from distdens.io import QuadratTableReader
import numpy as np
import utm

data = {
    "Area_del_cuadrante": [4, 4, 4],
    "Especie": ["Synthliboramphus hypoleucus", "Synthliboramphus hypoleucus", "Especie2"],
    "Este": [374448, 374458, 374542],
    "Madrigueras_con_actividad_aparente": [0, 1, 2],
    "Norte": [3198223, 3198229, 3198266],
    "Sitio_o_colonia": ["Morro Prieto", "Sitio2", "Morro Prieto"],
    "Zona_utm": ["11R", "11R", "11R"]
}

datos = pd.DataFrame(data)

filtro = {"Sitio_o_colonia": "Morro Prieto", "Especie": "Synthliboramphus hypoleucus"}


class TestQuadratTableReader(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        self.cuadrantes = QuadratTableReader.read(datos, filtro)
        self.LectorTablaCuadrante = QuadratTableReader()
        self.lon = np.array(
            np.array(
                utm.to_latlon(
                    data["Este"][0],
                    data["Norte"][0],
                    int(data["Zona_utm"][0][:-1]),
                    data["Zona_utm"][0][-1],
                )
            )[1]
        )

    def test_get_density(self):
        """
        Verifica que la densidad de calcule de manera correcta
        """
        self.assertTrue(type(self.cuadrantes).__name__ == "ndarray")

    def test_filter(self):
        """
        Verifica que la densidad de calcule de manera correcta
        """
        self.assertTrue(
            QuadratTableReader._filter_table(datos, filtro).Especie[0]
            == "Synthliboramphus hypoleucus"
        )

    def test_isStaticMethod_filter_table(self):
        """
        Verifica que la densidad de calcule de manera correcta
        """
        self.LectorTablaCuadrante._filter_table(datos, filtro)
        pass

    def test_isStaticMethod_create_quadrats_list(self):
        """
        Verifica que la densidad de calcule de manera correcta
        """
        data = QuadratTableReader._filter_table(datos, filtro)
        self.LectorTablaCuadrante._create_quadrats_list(data)
        pass

    def test_isStaticMethod_read(self):
        """
        Verifica que la densidad de calcule de manera correcta
        """
        self.LectorTablaCuadrante.read(datos, filtro)
        pass

    def test_isTheRightUTMZone(self):
        """
        Verifica que la densidad de calcule de manera correcta
        """
        """
        Verifica que la zona UTM es la correcta
        """
        self.assertTrue(self.lon == self.cuadrantes[0].lon)


if __name__ == "__main__":
    unittest.main()
