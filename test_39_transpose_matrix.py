import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

module = importlib.import_module("39_transpose_matrix")


def test_rectangular_matrix():
    assert module.transpose([[1, 2, 3], [4, 5, 6]]) == [
        [1, 4], [2, 5], [3, 6]
    ]


def test_square_matrix():
    assert module.transpose([[1, 2], [3, 4]]) == [
        [1, 3], [2, 4]
    ]


def test_single_row():
    assert module.transpose([[1, 2, 3]]) == [
        [1], [2], [3]
    ]


def test_single_column():
    assert module.transpose([[1], [2], [3]]) == [
        [1, 2, 3]
    ]


def test_empty_matrix():
    assert module.transpose([]) == []
