import sys
import pytest
from FirstUniqueChar import main as FirstUniqueChar
from NearestZeroSumTwo import main as NearestZeroSumTwo

#would be safer to use monkeypatch to change sys.argv

def test_FirstUniqueChar():
    sys.argv = ["", "abcda"]
    r1 = FirstUniqueChar()

    sys.argv = ["", "aabccdab"]
    r2 = FirstUniqueChar()

    sys.argv = ["", "adabccdab"]
    r3 = FirstUniqueChar()

    assert r1 == "b" and r2 == "d" and r3 == None

def test_NearestZeroSumTwo():
    sys.argv = ["", "-10", "-3", "1", "4", "8"]

    r1 = NearestZeroSumTwo()

    assert r1 == (-3,4) or r1 == (4,-3)

    sys.argv = ["", "4", "7", "2"]

    r2 = NearestZeroSumTwo()

    assert r2 == (4,2) or r2 == (2,4)