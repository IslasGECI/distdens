import numpy as np
import pandas as pd
import utm
from distdens.io import QuadratTableReader

data = {
    "Area_del_cuadrante": [4, 4, 4],
    "Especie": [
        "Synthliboramphus hypoleucus",
        "Synthliboramphus hypoleucus",
        "Especie2",
    ],
    "Este": [374448, 374458, 374542],
    "Madrigueras_con_actividad_aparente": [0, 1, 2],
    "Norte": [3198223, 3198229, 3198266],
    "Sitio_o_colonia": ["Morro Prieto", "Sitio2", "Morro Prieto"],
    "Zona_utm": ["11R", "11R", "11R"],
}

datos = pd.DataFrame(data)

filtro = {"Sitio_o_colonia": "Morro Prieto", "Especie": "Synthliboramphus hypoleucus"}


"""
Crea variables que se usarán en las pruebas
"""
cuadrantes = QuadratTableReader.read(datos, filtro)
LectorTablaCuadrante = QuadratTableReader()
lon = np.array(
    np.array(
        utm.to_latlon(
            data["Este"][0],
            data["Norte"][0],
            int(data["Zona_utm"][0][:-1]),
            data["Zona_utm"][0][-1],
        )
    )[1]
)


def test_get_density():
    """
    Verifica que la densidad de calcule de manera correcta
    """
    assert type(cuadrantes).__name__ == "ndarray"


def test_filter():
    """
    Verifica que la densidad de calcule de manera correcta
    """
    is_expected_specie = (
        QuadratTableReader._filter_table(datos, filtro).Especie[0] == "Synthliboramphus hypoleucus"
    )
    assert is_expected_specie


def test_isStaticMethod_filter_table():
    """
    Verifica que la densidad de calcule de manera correcta
    """
    LectorTablaCuadrante._filter_table(datos, filtro)
    pass


def test_isStaticMethod_create_quadrats_list():
    """
    Verifica que la densidad de calcule de manera correcta
    """
    data = QuadratTableReader._filter_table(datos, filtro)
    LectorTablaCuadrante._create_quadrats_list(data)
    pass


def test_isStaticMethod_read():
    """
    Verifica que la densidad de calcule de manera correcta
    """
    LectorTablaCuadrante.read(datos, filtro)
    pass


def test_isTheRightUTMZone():
    """
    Verifica que la zona UTM es la correcta
    """
    assert lon == cuadrantes[0].lon
