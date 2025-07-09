"""
An array is given of n length, and we need to calculate the next greater element for each element in the given array.
If the next greater element is not available in the given array then we need to fill '_' at that index place.

e.g:
Input :  6 3 9 8 10 2 1 15 7 
Output : 7 6 10 9 15 3 2 _ 8
"""

import sys
from bisect import bisect_left

# O(n*lg n) time complexity, assuming sorted(arr) is O(n*lg n) and bisect is O(lg n)
# O(n) space complexity
def SmallestGreatestElements(arr : list[int]):
    orderedArr = sorted(arr)
    
    for i in range(len(arr)):
        j = bisect_left(orderedArr, arr[i]) + 1

        if j < len(arr):
            arr[i] = orderedArr[j]
        else:
            arr[i] = "_"

def main():
    arr = list(map(int, sys.argv[1:]))

    SmallestGreatestElements(arr)

    print(arr)
    return arr

if __name__ == "__main__":
    main()