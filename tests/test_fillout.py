from distdens import fillout
import numpy as np


def test_fillout_start_left_down():
    x_expected = np.array([[0], [0], [1], [1], [0], [0], [0], [0], [1], [1], [0]])
    y_expected = np.array([[0], [1], [1], [0], [0], [0], [0], [1], [1], [0], [0]])
    x_in = np.array([0, 1, 1, 0, 0])
    y_in = np.array([0, 0, 1, 1, 0])
    x_obtained, y_obtained = fillout(x_in, y_in)
    print(x_obtained)
    print(y_obtained)
    np.testing.assert_equal(x_expected, x_obtained)
    np.testing.assert_equal(y_expected, y_obtained)


def test_fillout_start_right_up():
    x_expected = np.array([[0], [0], [1], [1], [0], [0], [1], [1], [1], [0], [0]])
    y_expected = np.array([[0], [1], [1], [0], [0], [0], [0], [1], [1], [1], [0]])
    x_in = np.array([1, 1, 0, 0, 1])
    y_in = np.array([1, 0, 0, 1, 1])
    x_obtained, y_obtained = fillout(x_in, y_in)
    print(x_obtained)
    print(y_obtained)
    np.testing.assert_equal(x_expected, x_obtained)
    np.testing.assert_equal(y_expected, y_obtained)
