import sys
import pytest

from Python.Misc.FirstUniqueChar import main as FirstUniqueChar
from Python.Misc.AngleHourAndMinute import main as AngleHourAndMinute
from Python.Misc.NthEvenFibNum import main as NthEvenFibNum
from Python.Misc.FibMemo import main as FibMemo
from Python.Misc.NQueens import main as NQueens
from Python.Misc.LongestCommonPrefix import main as LongestCommonPrefix
from Python.Misc.AtoiImplementation import main as AtoiImplementation
from Python.Misc.LargestHistogramArea import main as LargestHistogramArea
from Python.Misc.ZeroSumTriplet import main as ZeroSumTriplet
from Python.Misc.MaximumDifference import main as MaximumDifference

from Python.Sorting.BinaryArrSort import main as BinaryArrSort
from Python.Sorting.Sort0s1s2s import main as Sort0s1s2s
from Python.Sorting.MergeSort import main as MergeSort
from Python.Sorting.QuickSort import main as QuickSort
from Python.Sorting.BubbleSort import main as BubbleSort
from Python.Sorting.InsertionSort import main as InsertionSort
from Python.Sorting.SelectionSort import main as SelectionSort
from Python.Sorting.MergeSortedLinkedLists import main as MergeSortedLinkedLists

from Python.Arrays.ProductArray import main as ProductArray
from Python.Arrays.RotateArray import main as RotateArray
from Python.Arrays.RotateArrayNoAuxiliarSpace import main as RotateArrayNAS
from Python.Arrays.MaximumNonNegativeSubArray import main as MaximumNNSubArray
from Python.Arrays.MaximumSubArray import main as MaximumSubArray
from Python.Arrays.AllSubArrays import main as AllSubArrays
from Python.Arrays.AllSubsets import main as AllSubsets
from Python.Arrays.SubsetSum import main as SubsetSum
from Python.Arrays.NearestZeroSumTwo import main as NearestZeroSumTwo
from Python.Arrays.Partition import main as Partition
from Python.Arrays.IsPartition import main as IsPartition
from Python.Arrays.SmallestGreatestElements import main as SmallestGreatestElements
from Python.Arrays.LeftNearestSmallerNumbers import main as LeftNearestSmallerNumbers
from Python.Arrays.CountingInTwoArrays import main as CountingInTwoArrays

from Python.Matrices.MaxRectangle import main as MaxRectangle

#would be safer to use monkeypatch to change sys.argv

def test_FibMemo():
    sys.argv = ["", "0"]
    r1 = FibMemo()

    sys.argv = ["", "1"]
    r2 = FibMemo()

    sys.argv = ["", "20"]
    r3 = FibMemo()

    assert r1 == (0, 0, 0) and r2 == (1, 1, 1) and r3 == (6765, 6765, 6765)

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
    assert r1 == (-2, -2, -2)

    sys.argv = ["", "4", "-5", "2", "-1", "10", "-5", "6"]

    r2 = MaximumSubArray()
    assert r2 == (12, 12, 12)

    sys.argv = ["", "1", "2", "0", "12", "3", "4", "0"]

    r3 = MaximumSubArray()
    assert r3 == (22, 22, 22)

def test_AllSubArrays():
    sys.argv = ["", "1", "2", "3", "4"]

    r1 = AllSubArrays()
    output1 = [["1"], ["1", "2"], ["1", "2", "3"], ["1", "2", "3", "4"], ["2"], ["2", "3"], ["2", "3", "4"], ["3"], ["3", "4"], ["4"]]
    assert r1 == (output1, output1)

    sys.argv = ["", "1"]

    r2 = AllSubArrays()
    output2 = [["1"]]
    assert r2 == (output2, output2)

def test_AllSubsets():
    sys.argv = [""]

    r11, r12 = AllSubsets()
    output1 = [[]]
    assert (r11, r12) == (output1, output1)

    sys.argv = ["", "1", "2", "3"]

    r21, r22 = AllSubsets()
    r21 = sorted([sorted(l) for l in r21])
    r22 = sorted([sorted(l) for l in r22])

    output2 = sorted([["1"], ["2"], ["3"], ["1", "2"], ["1", "3"], ["2","3"], ["1", "2", "3"],[]])
    assert (r21, r22) == (output2, output2)

def test_SubsetSum():
    sys.argv = ["", "1", "-2", "4", "0", "-3", "7", "5", "-8", "17"]

    r11, r12, r13 = SubsetSum()
    assert (r11, r12, r13) == (True, True, True)

    sys.argv = ["", "1", "-2", "4", "0", "-3", "7", "5", "-8", "-5"]

    r21, r22, r23 = SubsetSum()
    assert (r21, r22, r23) == (True, True, True)

    sys.argv = ["", "1", "-2", "4", "0", "-3", "7", "5", "-8", "18"]

    r31, r32, r33 = SubsetSum()
    assert (r31, r32, r33) == (False, False, False)

def test_NQueens():
    sys.argv = ["", "3"]

    f1, _ = NQueens()

    assert f1 == False

    sys.argv = ["", "4"]

    f2, ret2 = NQueens()

    assert f2 == True and ret2 == [(1, 0), (3, 1), (0, 2), (2, 3)]

def test_SortingAlgorithms():
    sys.argv = [""]
    r11 = BubbleSort()
    r12 = InsertionSort()
    r13 = SelectionSort()
    r14 = MergeSort()
    r15 = QuickSort()
    assert r11 == r12 == r13 == r14 == r15 == []

    sys.argv = ["", "1"]
    r21 = BubbleSort()
    r22 = InsertionSort()
    r23 = SelectionSort()
    r24 = MergeSort()
    r25 = QuickSort()
    assert r21 == r22 == r23 == r24 == r25 == [1]

    sys.argv = ["", "3", "5", "1", "4", "2"]
    r31 = BubbleSort()
    r32 = InsertionSort()
    r33 = SelectionSort()
    r34 = MergeSort()
    r35 = QuickSort()
    assert r31 == r32 == r33 == r34 == r35 == [1, 2, 3, 4, 5]

def test_BinaryArrSort():
    sys.argv = [""]
    r1 = BinaryArrSort()
    assert r1 == []

    sys.argv = ["", "1", "0", "1", "1", "0"]
    r2 = BinaryArrSort()
    assert r2 == [0, 0, 1, 1, 1]

def test_Sort0s1s2s():
    sys.argv = [""]
    r1 = Sort0s1s2s()
    assert r1 == []

    sys.argv = ["", "0", "1", "1", "0", "1", "2", "1", "2", "0", "0", "0", "1"]
    r2 = Sort0s1s2s()
    assert r2 == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]

def test_IsPartition():
    sys.argv = ["", "continue"]
    r1 = IsPartition()
    assert r1 == True

    sys.argv = ["", "1", "continue", "1"]
    r2 = IsPartition()
    assert r2 == True

    sys.argv = ["", "1", "continue", "2"]
    r3 = IsPartition()
    assert r3 == False

    sys.argv = ["", "1", "1", "continue", "1"]
    r4 = IsPartition()
    assert r4 == False

    sys.argv = ["", "2", "0", "1", "3", "5", "4", "continue", "3", "4", "1", "5", "2", "0"]
    r5 = IsPartition()
    assert r5 == True

    sys.argv = ["", "2", "1", "3", "continue", "2", "3", "1"]
    r6 = IsPartition()
    assert r6 == False

    sys.argv = ["", "5", "4", "5", "6", "continue", "5", "4", "5", "6"]
    r7 = IsPartition()
    assert r7 == True

    sys.argv = ["", "5", "4", "5", "6", "5", "continue", "5", "4", "5", "6", "5"]
    r8 = IsPartition()
    assert r8 == True

    sys.argv = ["", "5", "6", "5", "4", "5", "continue", "5", "6", "5", "4", "5"]
    r9 = IsPartition()
    assert r9 == False

def test_Partition():
    sys.argv = [""]
    r11, r12, r13 = Partition()
    assert r11 == r12 == r13 == []

    sys.argv = ["", "1"]
    r21, r22, r23 = Partition()
    assert r21 == r22 == r23 == [1]

    sys.argv = ["", "3", "4", "1", "2", "5", "0"]
    arrArg = [3, 4, 1, 2, 5, 0]
    r31, r32, r33 = Partition()
    assert IsPartition(r31, arrArg) and IsPartition(r32, arrArg) and IsPartition(r33, arrArg)

def test_LongestCommonPrefix():
    sys.argv = ["", "geeks", "dgeek"]
    r1 = LongestCommonPrefix()

    sys.argv = ["", "practicegeeks", "coderpractice"]
    r2 = LongestCommonPrefix()

    sys.argv = ["", "ggeggksyabcdef", "agaggeggeggksy"]
    r3 = LongestCommonPrefix()

    sys.argv = ["", "abcdef", "bbbccc"]
    r4 = LongestCommonPrefix()

    assert r1 == 4 and r2 == 8 and r3 == 8 and r4 == 0

def test_AtoiImplementation():
    sys.argv = ["", "-123"]
    r1 = AtoiImplementation()

    sys.argv = ["", "   -"]
    r2 = AtoiImplementation()

    sys.argv = ["", " 1231231231311133"]
    r3 = AtoiImplementation()

    sys.argv = ["", "-999999999999"]
    r4 = AtoiImplementation()

    sys.argv = ["", "  -0012gfg4"]
    r5 = AtoiImplementation()

    assert r1 == -123 and r2 == 0 and r3 == (2**31)-1 and r4 == -(2**31) and r5 == -12

def test_SmallestGreatestElements():
    sys.argv = ["", "6", "3", "9", "8", "10", "2", "1", "15", "7"]
    r1 = SmallestGreatestElements()

    sys.argv = ["", "13", "6", "7", "12"]
    r2 = SmallestGreatestElements()

    sys.argv = ["", "1"]
    r3 = SmallestGreatestElements()

    sys.argv = [""]
    r4 = SmallestGreatestElements()
    
    assert (r1 == [7, 6, 10, 9, 15, 3, 2, "_", 8]
            and r2 == ["_", 7, 12, 13]
            and r3 == ["_"]
            and r4 == [])
    
def test_MaxRectangle():
    sys.argv = ["", "1", "1", "0", "0", "0", "1", "b",
                    "0", "1", "1", "0", "0", "1", "b",
                    "0", "0", "1", "1", "0", "1"]
    r1 = MaxRectangle()

    sys.argv = ["", "0", "1", "1", "0", "b",
                    "1", "1", "1", "1", "b",
                    "1", "1", "1", "1", "b",
                    "1", "1", "0", "0"]
    r2 = MaxRectangle()

    sys.argv = ["", "0", "1", "1", "b",
                    "1", "1", "1", "b",
                    "0", "1", "1"]
    r3 = MaxRectangle()

    assert r1 == 3 and r2 == 8 and r3 == 6

def test_LargestHistogramArea():
    sys.argv = [""]
    r1 = LargestHistogramArea()

    sys.argv = ["", "10"]
    r2 = LargestHistogramArea()

    sys.argv = ["", "60", "20", "50", "40", "10", "50", "60"]
    r3 = LargestHistogramArea()

    assert r1 == -1 and r2 == 10 and r3 == 100

def test_LeftNearestSmallerNumbers():
    sys.argv = ["", "1", "6", "2"]
    r1 = LeftNearestSmallerNumbers()

    sys.argv = ["", "1", "5", "0", "3", "4", "5"]
    r2 = LeftNearestSmallerNumbers()

    assert r1 == [-1, 1, 1] and r2 == [-1, 1, -1, 0, 3, 4]

def test_ZeroSumTriplet():
    sys.argv = ["", "0", "-1", "2", "-3", "1"]
    r1 = ZeroSumTriplet()

    sys.argv = ["", "1", "2", "3"]
    r2 = ZeroSumTriplet()

    assert r1 == True and r2 == False

def test_CountingInTwoArrays():
    sys.argv = ["", "4", "8", "7", "-1", "5", "1", "b",
                    "4", "48", "3", "0", "1", "1", "5"]
    
    r = CountingInTwoArrays()

    assert r == [5, 6, 6, 0, 6, 3]

def test_MergeSortedLinkedLists():
    sys.argv = ["", "1", "3", "b", "8", "b", "4", "5", "6"]

    assert MergeSortedLinkedLists() == [1, 3, 4, 5, 6, 8]

def test_MaximumDifference():
    sys.argv = ["", "2", "4", "8", "7", "7", "9", "3"]

    assert MaximumDifference() == 4
