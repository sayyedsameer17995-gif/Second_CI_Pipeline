import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

module = importlib.import_module("35_move_zeros")


def test_zeros_at_beginning():
    assert module.move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]


def test_zeros_at_end():
    assert module.move_zeros([1, 2, 0, 0]) == [1, 2, 0, 0]


def test_no_zeros():
    assert module.move_zeros([1, 2, 3]) == [1, 2, 3]


def test_all_zeros():
    assert module.move_zeros([0, 0, 0]) == [0, 0, 0]


def test_empty_list():
    assert module.move_zeros([]) == []
