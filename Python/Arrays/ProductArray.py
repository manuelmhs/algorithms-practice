"""
Given an array arr[], construct a product array res[], where each element in res[i] is the product of all elements in arr[] except arr[i].
Return this resultant array, res[].
arr.size() >= 2
"""

import sys

def main():
    arr = list(map(int, sys.argv[1:]))
    total = 1
    zeroesCount = 0

    for n in arr:
        if n == 0 and zeroesCount == 0:
            zeroesCount += 1
            continue
        elif n == 0 and zeroesCount == 1:
            zeroesCount += 1
            total = 0
            break
        else:
            total *= n
    

    res = [None] * len(arr)
    for i, n in enumerate(arr):
        if n == 0:
            res[i] = total
        else:
            if zeroesCount == 0:
                res[i] = total // n
            elif zeroesCount >= 1:
                res[i] = 0

    print(res)
    return res

if __name__ == "__main__":
    main()