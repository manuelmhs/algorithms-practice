import sys
import pytest
from Python.FirstUniqueChar import main as FirstUniqueChar
from Python.NearestZeroSumTwo import main as NearestZeroSumTwo
from Python.AngleHourAndMinute import main as AngleHourAndMinute
from Python.NthEvenFibNum import main as NthEvenFibNum
from Python.ProductArray import main as ProductArray
from Python.RotateArray import main as RotateArray
from Python.RotateArrayNoAuxiliarSpace import main as RotateArrayNAS
from Python.MaximumNonNegativeSubArray import main as MaximumNNSubArray
from Python.MaximumSubArray import main as MaximumSubArray

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

def test_AngleHourAndMinute():
    sys.argv = ["", "3", "30"]

    r1 = AngleHourAndMinute()
    assert r1 == 75

    sys.argv = ["", "9", "0"]

    r2 = AngleHourAndMinute()
    assert r2 == 90

def test_NthEvenFibNum():
    sys.argv = ["", "1"]

    r1 = NthEvenFibNum()
    assert r1 == 2

    sys.argv = ["", "4"]

    r2 = NthEvenFibNum()
    assert r2 == 144

def test_ProductArray():
    sys.argv = ["", "10", "3", "5", "6", "2"]

    r1 = ProductArray()
    assert r1 == [180, 600, 360, 300, 900]

    sys.argv = ["", "12", "0"]

    r2 = ProductArray()
    assert r2 == [0, 12]

    sys.argv = ["", "1", "0", "7", "0", "-2"]

    r3 = ProductArray()
    assert r3 == [0, 0, 0, 0, 0]

def test_RotateArray():
    sys.argv = ["", "1", "2", "3", "4", "1"]

    r1 = RotateArray()
    assert r1 == [2, 3, 4, 1]

    sys.argv = ["", "1", "2", "3", "4", "2"]

    r2 = RotateArray()
    assert r2 == [3, 4, 1, 2]

    sys.argv = ["", "1", "2", "3", "4", "3"]

    r3 = RotateArray()
    assert r3 == [4, 1, 2, 3]

    sys.argv = ["", "1", "2", "3", "4", "4"]

    r4 = RotateArray()
    assert r4 == [1, 2, 3, 4]

def test_RotateArray():
    sys.argv = ["", "1", "2", "3", "4", "1"]

    r1 = RotateArray()
    assert r1 == [2, 3, 4, 1]

    sys.argv = ["", "1", "2", "3", "4", "2"]

    r2 = RotateArray()
    assert r2 == [3, 4, 1, 2]

    sys.argv = ["", "1", "2", "3", "4", "3"]

    r3 = RotateArray()
    assert r3 == [4, 1, 2, 3]

    sys.argv = ["", "1", "2", "3", "4", "4"]

    r4 = RotateArray()
    assert r4 == [1, 2, 3, 4]

def test_RotateArrayNAS():
    sys.argv = ["", "1", "2", "3", "4", "1"]

    r1 = RotateArrayNAS()
    assert r1 == [4, 1, 2, 3]

    sys.argv = ["", "1", "2", "3", "4", "2"]

    r2 = RotateArrayNAS()
    assert r2 == [3, 4, 1, 2]

    sys.argv = ["", "1", "2", "3", "4", "3"]

    r3 = RotateArrayNAS()
    assert r3 == [2, 3, 4, 1]

    sys.argv = ["", "1", "2", "3", "4", "4"]

    r4 = RotateArrayNAS()
    assert r4 == [1, 2, 3, 4]

def test_MaximumNNSubArray():
    sys.argv = ["", "-1", "-5", "-2"]

    r1 = MaximumNNSubArray()
    assert r1 == -1

    sys.argv = ["", "1", "5", "-2", "0", "6", "-3", "-3", "4", "2"]

    r2 = MaximumNNSubArray()
    assert r2 == [1, 5]

    sys.argv = ["", "1", "2", "-1", "3" , "1"]

    r3 = MaximumNNSubArray()
    assert r3 == [3, 1]

def test_MaximumSubArray():
    sys.argv = ["", "-10", "-2", "-15"]

    r1 = MaximumSubArray()
    assert r1 == -2

    sys.argv = ["", "4", "-5", "2", "-1", "10", "-5", "6"]

    r2 = MaximumSubArray()
    assert r2 == 12

    sys.argv = ["", "1", "2", "0", "12", "3", "4", "0"]

    r3 = MaximumSubArray()
    assert r3 == 22