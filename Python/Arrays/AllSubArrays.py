"""
Given an array arr[], return a new array res[] that contains all possible subarrays of arr[].
Assume arr[] is non-empty.

e.g:
arr = [1,2,3,4]
res = [[1], [1,2], [1,2,3], [1,2,3,4], [2], [2,3], [2,3,4], [3], [3,4], [4]]
"""

import sys
from math import floor

def iterative(arr):
    l = len(arr)
    res = [None] * int((l * (l+1)) / 2)

    idxLast = 0
    for i, x in enumerate(arr):
        res[idxLast] = [x]
        idxLast += 1
        for j, y in enumerate(arr[i+1:]):
            res[idxLast] = res[idxLast-1] + [y]
            idxLast += 1

    return res

def recursive(arr):
    l = len(arr)
    elem = arr[0]

    if (l == 1):
        return [[elem]]
    else:
        r = recursive(arr[1:])
        k = l-1
        return [[elem]] + list(map(lambda array: [elem] + array, r[:k])) + r

def main():
    arr = sys.argv[1:]

    resIter = iterative(arr)
    resRec = recursive(arr)
    
    print(resIter)
    print(resRec)
    return (resIter, resRec)

if __name__ == "__main__":
    main()