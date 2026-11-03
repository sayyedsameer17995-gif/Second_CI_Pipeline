import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

module = importlib.import_module("38_missing_number_xor")


def test_missing_middle_number():
    assert module.missing_number([0, 1, 3, 4]) == 2


def test_missing_first_number():
    assert module.missing_number([1, 2, 3]) == 0


def test_missing_last_number():
    assert module.missing_number([0, 1, 2, 3]) == 4


def test_single_element_list():
    assert module.missing_number([0]) == 1


def test_empty_list():
    assert module.missing_number([]) == 0
