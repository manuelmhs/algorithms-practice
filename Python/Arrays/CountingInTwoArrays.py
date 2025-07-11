"""
You are given two unsorted arrays a[] and b[]. Both arrays may contain duplicate elements.
For each element in a[], your task is to count how many elements in b[] are less than or equal to that element.

Input: a[] = [4, 8, 7, -1, 5, 1], b[] = [4, 48, 3, 0, 1, 1, 5]
Output: [5, 6, 6, 0, 6, 3]
"""

import sys
from bisect import bisect_right

# Time complexity: O((n+m)*lg m), Space complexity: O(n)
# idea: we sort b to use binary search. This way, instead of comparing each of a's element with each of b's (n*m comparisons),
# binary search guarantees lg m comparisons for each a's element (n*lg m comparisons)
def CountingInTwoArrays(a, b):
    b.sort() # m * lg m

    l = len(a)
    res = [None] * l
    for i, e in enumerate(a): # n
        # bisect_right returns an idx such that b[i] <= e for each i < idx
        idx = bisect_right(b, e) # lg m
        res[i] = idx
    # m*lg m + n*lg m = (n+m)*lg m

    return res

def main():
    a = []
    b = []

    ptr = a
    for x in sys.argv[1:]:
        if x == "b":
            ptr = b
        else:
            ptr.append(int(x))

    res = CountingInTwoArrays(a, b)

    print(res)
    return res

if __name__ == "__main__":
    main()