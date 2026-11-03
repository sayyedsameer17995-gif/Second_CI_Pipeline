import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

module = importlib.import_module("40_gcd")


def test_normal_numbers():
    assert module.gcd(12, 18) == 6


def test_coprime_numbers():
    assert module.gcd(7, 9) == 1

def test_negative_numbers():
    assert module.gcd(-12, 18) == 6
def test_same_numbers():
    assert module.gcd(10, 10) == 10


def test_zero():
    assert module.gcd(0, 5) == 5
