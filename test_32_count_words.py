import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

module = importlib.import_module("32_count_words")


def test_normal_sentence():
    assert module.count_words("Python is easy") == 3


def test_empty_string():
    assert module.count_words("") == 0


def test_single_word():
    assert module.count_words("Python") == 1


def test_multiple_spaces():
    assert module.count_words("Python   is   easy") == 3


def test_leading_and_trailing_spaces():
    assert module.count_words("  Python is easy  ") == 3
