import numpy as np
import matplotlib.pyplot as plt


def fillout(x, y, limits=None, **kwargs):
    if limits is None:
        limits = [min(x), max(x), min(y), max(y)]
    indice_pegado_costa = np.where(x == min(x))[0][0]
    closed_x = _close_coordinate(x, indice_pegado_costa)
    closed_y = _close_coordinate(y, indice_pegado_costa)
    x_prueba = _test_x(limits, closed_x)
    y_prueba = _test_y(limits, closed_y)
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


def _test_x(limits, closed):
    inicial = np.array(limits[0]).reshape(1, 1)
    final = np.array(limits[1]).reshape(1, 1)
    prueba = np.concatenate([inicial, inicial, final, final, inicial, _flip_closed(closed),])
    return prueba


def _test_y(limits, closed):
    inicial = np.array(limits[2]).reshape(1, 1)
    final = np.array(limits[3]).reshape(1, 1)
    prueba = np.concatenate([inicial, final, final, inicial, inicial, _flip_closed(closed),])
    return prueba
