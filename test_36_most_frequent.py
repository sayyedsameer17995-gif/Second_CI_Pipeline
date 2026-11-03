import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

module = importlib.import_module("36_most_frequent")


def test_normal_list():
    assert module.most_frequent([1, 2, 2, 3, 2]) == 2


def test_single_element():
    assert module.most_frequent([5]) == 5


def test_all_same_elements():
    assert module.most_frequent([4, 4, 4]) == 4


def test_tie_returns_first_occurring():
    assert module.most_frequent([1, 2, 1, 2]) == 1


def test_empty_list():
    assert module.most_frequent([]) is None
