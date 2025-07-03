"""
Given an array arr[], rotate the array to the right (clockwise direction) by d steps, where d is a positive integer.
Do the mentioned change in the array in place, without auxiliar space used (O(1)).
Note: consider the array as circular
"""

import sys
from math import floor

#FlipArray should modify the original arr to achieve O(1) auxiliar space, this is a simplification
#could be achieved by passing arr, start, len (or finish) to the FlipArray function
def FlipArray(arr):
    l = len(arr)

    if l <= 1:
        return arr
    else:
        k = floor(l / 2)

        for i in range(k):
            j = l-i-1

            aux = arr[i]
            arr[i] = arr[j]
            arr[j] = aux

    return arr

def main():
    arr = list(map(int, sys.argv[1:-1]))
    d = int(sys.argv[-1])

    l = len(arr)
    d = d % l

    fin = arr
    if d > 0:
        arr1 = FlipArray(arr[:l-d])
        arr2 = FlipArray(arr[l-d:])
        fin = FlipArray(arr1 + arr2)

    print(fin)
    return fin

if __name__ == "__main__":
    main()