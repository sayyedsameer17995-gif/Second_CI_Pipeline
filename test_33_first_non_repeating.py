import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

module = importlib.import_module("33_first_non_repeating")


def test_swiss():
    assert module.first_non_repeating("swiss") == "w"


def test_hello():
    assert module.first_non_repeating("hello") == "h"


def test_all_repeated():
    assert module.first_non_repeating("aabbcc") is None


def test_single_character():
    assert module.first_non_repeating("a") == "a"


def test_empty_string():
    assert module.first_non_repeating("") is None
