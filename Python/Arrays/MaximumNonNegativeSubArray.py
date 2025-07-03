"""
Given an array of integers arr[], find the contiguous subarray with the maximum sum that contains only non-negative numbers.
If multiple subarrays have the same sum, return the one with the smallest starting index.
If the array contains only negative numbers, return -1.

Note: A subarray is a contiguous non-empty sequence of elements within an array.
"""

import sys

def main():
    arr = list(map(int, sys.argv[1:]))

    start = end = max = tempStart = tempEnd = tempSum = -1
    for i, n in enumerate(arr):
        if n >= 0:
            if tempStart == -1:
                tempStart = i
                tempEnd = i
                tempSum = n
            else:
                tempEnd = i
                tempSum += n
        else:
            if tempSum > max:
                max = tempSum
                start = tempStart
                end = tempEnd

            tempStart = tempEnd = tempSum = -1

    if tempSum > max:
        max = tempSum
        start = tempStart
        end = tempEnd

    res = None
    if (max == -1):
        res = -1
    else:
        res = arr[start:end+1]
        
    print(res)
    return res

if __name__ == "__main__":
    main()