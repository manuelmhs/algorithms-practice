import sys
import pytest
from FirstUniqueChar import main as FirstUniqueChar

def test_FirstUniqueChar():
    sys.argv[1] = "abcda"
    r1 = FirstUniqueChar()

    sys.argv[1] = "aabccdab"
    r2 = FirstUniqueChar()

    sys.argv[1] = "adabccdab"
    r3 = FirstUniqueChar()

    assert r1 == "b" and r2 == "d" and r3 == None