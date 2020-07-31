import numpy as np
import matplotlib.pyplot as plt


def fillout(x, y, limits=None, **kwargs):
    if limits is None:
        limits = [min(x), max(x), min(y), max(y)]
    x_inicial = np.array(limits[0]).reshape(1, 1)
    x_final = np.array(limits[1]).reshape(1, 1)
    y_inicial = np.array(limits[2]).reshape(1, 1)
    y_final = np.array(limits[3]).reshape(1, 1)
    indice_pegado_costa = np.where(x == min(x))[0][0]
    closed_x = _close_coordinate(x, indice_pegado_costa)
    closed_y = _close_coordinate(y, indice_pegado_costa)
    x_prueba = np.concatenate(
        [
            x_inicial,
            x_inicial,
            x_final,
            x_final,
            x_inicial,
            _flip_closed(closed_x),
        ]
    )
    y_prueba = np.concatenate(
        [
            y_inicial,
            y_final,
            y_final,
            y_inicial,
            y_inicial,
            _flip_closed(closed_y),
        ]
    )
    plt.fill(x_prueba, y_prueba, **kwargs)
    return x_prueba, y_prueba


def _close_coordinate(coordinate, indice_pegado_costa):
    closed_coordinate = np.concatenate(
        [
            coordinate[indice_pegado_costa:].reshape(len(coordinate[indice_pegado_costa:]), 1),
            coordinate[0:indice_pegado_costa].reshape(len(coordinate[0:indice_pegado_costa]), 1),
            coordinate[indice_pegado_costa].reshape(1, 1),
        ]
    )
    return closed_coordinate


def _flip_closed(closed):
    flipped_closed = np.flip(closed.reshape(len(closed), 1))
    return flipped_closed
