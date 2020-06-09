from distdens import fillout
import numpy as np


def test_fillout():
    x = np.array([0, 1, 1, 0, 0])
    y = np.array([0, 0, 1, 1, 0])
    fillout(x, y)
