"""
Given an array arr[], return a new array res[] that contains all possible subsets of arr[].

e.g:
arr = [1,2,3]
res = [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
"""

import sys
from math import floor

def iterative(arr):
    res = []
    for i, x in enumerate(arr):
        res = [[x]] + res + list(map(lambda arr: arr + [x], res[:]))

    return [[]] + res

def aux(arr):
    l = len(arr)

    if (l == 0):
        return []
    elif (l == 1):
        elem = arr[0]

        return [[elem]]
    else:
        elem = arr[0]

        r = aux(arr[1:])
        return [[elem]] + r + list(map(lambda arr: [elem] + arr, r[:]))

def recursive(arr):
    return [[]] + aux(arr)

def main():
    arr = sys.argv[1:]

    resIter = iterative(arr)
    resRec = recursive(arr)
    
    print(resIter)
    print(resRec)
    return (resIter, resRec)

if __name__ == "__main__":
    main()