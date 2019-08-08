import numpy as np
import matplotlib.pyplot as plt


def fillout(x, y, limits=None, **kwargs):
    if limits is None:
        limits=[min(x), max(x), min(y), max(y)]
    x_inicial = np.array(limits[0]).reshape(1,1)
    x_final = np.array(limits[1]).reshape(1,1)
    y_inicial = np.array(limits[2]).reshape(1,1)
    y_final = np.array(limits[3]).reshape(1,1)
    indice_pegado_costa = np.where(x == min(x))[0][0]    
    x_cerrada = np.concatenate([x[indice_pegado_costa:].reshape(len(x[indice_pegado_costa:]), 1), x[0:indice_pegado_costa].reshape(len(x[0:indice_pegado_costa]), 1), x[indice_pegado_costa].reshape(1,1)])
    y_cerrada = np.concatenate([y[indice_pegado_costa:].reshape(len(y[indice_pegado_costa:]), 1), y[0:indice_pegado_costa].reshape(len(y[0:indice_pegado_costa]), 1), y[indice_pegado_costa].reshape(1,1)])
    x_prueba = np.concatenate([x_inicial,x_inicial,x_final,x_final,x_inicial,np.flip(x_cerrada.reshape(len(x_cerrada), 1))])
    y_prueba = np.concatenate([y_inicial,y_final,y_final,y_inicial,y_inicial,np.flip(y_cerrada.reshape(len(x_cerrada), 1))])
    plt.fill(x_prueba, y_prueba, **kwargs)
