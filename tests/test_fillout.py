from distdens import fillout
from distdens.fillout import _close_coordinate, _flip_closed, _test_x
import numpy as np


def test_fillout_start_left_down():
    x_expected = np.array([[0], [0], [1], [1], [0], [0], [0], [0], [1], [1], [0]])
    y_expected = np.array([[0], [1], [1], [0], [0], [0], [0], [1], [1], [0], [0]])
    x_in = np.array([0, 1, 1, 0, 0])
    y_in = np.array([0, 0, 1, 1, 0])
    x_obtained, y_obtained = fillout(x_in, y_in)
    np.testing.assert_equal(x_expected, x_obtained)
    np.testing.assert_equal(y_expected, y_obtained)


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


def test_test_x():
    limits: list = [0, 2, 0, 1]
    closed: np.array = np.array([[1], [2], [3], [1]])
    x_expected: np.array = np.array([[0], [0], [2], [2], [0], [1], [3], [2], [1]])
    x_obtained: np.array = _test_x(limits, closed)
    np.testing.assert_equal(x_expected, x_obtained)
