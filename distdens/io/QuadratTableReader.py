from abc import ABC
import numpy as np
import pandas as pd
import utm

from ..models import SamplingQuadrat


class QuadratTableReader(ABC):
    @staticmethod
    def read(quadrats_table: pd.DataFrame, filter_dict):
        data = QuadratTableReader._filter_table(quadrats_table, filter_dict)
        return QuadratTableReader._create_quadrats_list(data)

    @staticmethod
    def _filter_table(quadrats_table: pd.DataFrame, filter_dict) -> pd.DataFrame:
        data = quadrats_table
        for filter_argument in filter_dict.keys():
            data = data[data[f"{filter_argument}"]
                        == filter_dict[filter_argument]]
        return data

    @staticmethod
    def _create_quadrats_list(data: pd.DataFrame):
        return np.array([SamplingQuadrat(*utm.to_latlon(row.Este, row.Norte, int(row.Zona_utm[:-1]), row.Zona_utm[-1]), row.Area_del_cuadrante, row.Madrigueras_con_actividad_aparente) for _, row in data.iterrows()])        
