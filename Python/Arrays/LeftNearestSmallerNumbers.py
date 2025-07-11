"""
Given an array of integers, find the nearest smaller number for every element such that the smaller element is on the left side.

Input: arr = [1, 6, 2]
Output: [-1, 1, 1]

Input: arr = [1, 5, 0, 3, 4, 5]
Output: [-1, 1, -1, 0, 3, 4]
"""

import sys
from collections import deque

# the naive implementation would be pretty straightforward: two nested loops, in each step of the outer loop, the inner loop
# iters from that element, right to left, searching a smaller element. The first one encountered is the correct answer.
# this would lead to O(n^2) time complexity

# an improvement to the naive idea: we use only one loop, and we use a stack to push the elements we read. The key idea is
# that in each step, we compare our element with the first element of the stack (LIFO) and choose it if it's smaller than
# the current one. If not, we pop all greater values (and discard them) we come across until we empty the stack or reach a smaller one.
# This results in a ascending order stack (monotonic stack), and we discard unnecessary values, avoinding unnecessary comparisons in future iters.
# Time complexity: O(n) (amortized), Space complexity: O(n)
def stackImplementation(arr):
    l = len(arr)
    result = [None] * l
    q = deque() # deque supports O(1) push/pop operations
    for i in range(l):
        n = arr[i]

        # discard all greater values than the current one
        # this values can't be nearest smaller to any future element, would be absurd
        while len(q) > 0 and q[0] > n:
            q.popleft()
        
        nearest = -1
        if len(q) > 0:
            nearest = q[0]

        result[i] = nearest
        q.appendleft(n)

    return result

def main():
    arr = list(map(int, sys.argv[1:]))

    r = stackImplementation(arr)

    print(r)
    return r


if __name__ == "__main__":
    main()