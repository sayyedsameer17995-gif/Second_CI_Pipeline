import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

module = importlib.import_module("37_rotate_string")


def test_rotate_by_two():
    assert module.rotate_string("hello", 2) == "lohel"


def test_rotate_by_one():
    assert module.rotate_string("abcd", 1) == "dabc"


def test_rotate_by_full_length():
    assert module.rotate_string("python", 6) == "python"


def test_rotate_more_than_length():
    assert module.rotate_string("abcd", 6) == "cdab"


def test_empty_string():
    assert module.rotate_string("", 3) == ""
