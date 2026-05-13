import numpy as np
from distdens import fillout
from distdens.fillout import _close_coordinate, _flip_closed
import matplotlib


def test_fillout_start_left_down():
    x_expected = np.array([[0], [0], [1], [1], [0], [0], [0], [0], [1], [1], [0]])
    y_expected = np.array([[0], [1], [1], [0], [0], [0], [0], [1], [1], [0], [0]])
    x_in = np.array([0, 1, 1, 0, 0])
    y_in = np.array([0, 0, 1, 1, 0])
    color = "red"
    x_obtained, y_obtained = fillout(x_in, y_in, color=color)
    np.testing.assert_equal(x_expected, x_obtained)
    np.testing.assert_equal(y_expected, y_obtained)

    obtained_polygon = matplotlib.pyplot.gca().get_children()[0]
    isinstance(obtained_polygon, matplotlib.patches.Polygon)

    obtained_x_vertices = obtained_polygon.get_path().vertices[:, 0]
    assert all(obtained_x_vertices == x_expected[:, 0])

    assert obtained_polygon._original_edgecolor == color


def test_fillout_start_right_up():
    x_expected = np.array([[0], [0], [1], [1], [0], [0], [1], [1], [1], [0], [0]])
    y_expected = np.array([[0], [1], [1], [0], [0], [0], [0], [1], [1], [1], [0]])
    x_in = np.array([1, 1, 0, 0, 1])
    y_in = np.array([1, 0, 0, 1, 1])
    x_obtained, y_obtained = fillout(x_in, y_in)
    np.testing.assert_equal(x_expected, x_obtained)
    np.testing.assert_equal(y_expected, y_obtained)


def test_close_coordinate():
    x_in: np.array = np.array([1, 2, 3])
    index = np.where(x_in == min(x_in))[0][0]
    x_obtained: np.array = _close_coordinate(x_in, index)
    x_expected: np.array = np.array([[1], [2], [3], [1]])
    np.testing.assert_equal(x_expected, x_obtained)


def test_flip_closed():
    x_closed: np.array = np.array([[1], [2], [3], [1]])
    flipped_closed_tests: np.array = np.array([[1], [3], [2], [1]])
    flipped_closed = _flip_closed(x_closed)
    np.testing.assert_equal(flipped_closed, flipped_closed_tests)
