"""
Given an array of integers arr[], find the maximum contiguous sum (can be formed with both positive and negative numbers).
Assume arr[] is not empty.
"""

import sys
from math import floor

#W(n) = S(n) = n^2
def IterativeNaive(arr):
    partial = maximum = float('-inf')
    for i, n in enumerate(arr):
        partial = n
        maximum = max(partial, maximum)
        for j, m in enumerate(arr[i+1:]):
            partial += m
            maximum = max(partial, maximum)

    return maximum


#usage of Kadane's algorithm
#W(n) = S(n) = n
def Kadane(arr):
    partial = arr[0]
    maximum = arr[0]

    for n in arr[1:]: #this generates an unnecessary copy
        if partial >= 0:
            partial += n
        else:
            partial = n

        maximum = max(partial, maximum)

    return maximum

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

    m1 = IterativeNaive(arr)
    m2 = Kadane(arr)
    (m3, _, _, _) = MSB(arr)
    

    print(f"{m1}, {m2}, {m3}")
    return (m1, m2, m3)

if __name__ == "__main__":
    main()