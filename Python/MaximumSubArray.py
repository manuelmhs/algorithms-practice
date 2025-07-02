"""
Given an array of integers arr[], find the maximum contiguous sum (can be formed with both positive and negative numbers).
Assume arr[] is not empty.
"""

import sys
from math import floor

#usage of Divide and Conquer and tupling
#W(n) = n, S(n) = lg n

def MSB(arr):
    l = len(arr)
    if l == 1:
        return (arr[0], arr[0], arr[0], arr[0])
    else:
        mid = floor(l/2)

        (maximum1, prefix1, suffix1, total1) = MSB(arr[:mid])
        (maximum2, prefix2, suffix2, total2) = MSB(arr[mid:])

        prefix = max(prefix1, total1, total1 + prefix2, total1 + total2)
        suffix = max(suffix2, total2, total2 + suffix1, total1 + total2)
        total = total1 + total2
        maximum = max(maximum1, maximum2, suffix1 + prefix2,
                      suffix1 + total2, total1 + prefix2, total1 + total2)
        
        return (maximum, prefix, suffix, total)

def main():
    arr = list(map(int, sys.argv[1:]))

    (m, _, _, _) = MSB(arr)

    print(m)
    return m

if __name__ == "__main__":
    main()