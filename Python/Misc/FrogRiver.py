"""
------ Frog - River: ------

A small frog wants to get to the other side of a river. The frog is currently located at position 0, and wants to get to position X.
Leaves fall from a tree onto the surface of the river. You are given a non-empty zero-indexed array arr[] consisting of N integers representing the falling
leaves. arr[K] represents the position where one leaf falls at time K, measured in seconds. The goal is to find the earliest time when the frog can jump to
position X. The frog can jump J positions far. The leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5, J = 1 and array arr such that: 
A[0] = 1 A[1] = 3 A[2] = 1 A[3] = 4 A[4] = 2 A[5] = 3 A[6] = 5 A[7] = 4

In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river,
and the frog can jump to position X (5).

Write a function that returns the earliest time when the frog can jump to the other side of the river which is X wide.
If the frog is never able to jump to the other side of the river, the function should return −1.

If A[i] = -1, that means the ith leaf never fell.
"""

import sys

# if J = 1 (like some versions of this problem), this can be solved pretty easily in O(n) time and O(X) space, iterating through arr
# until we found all the numbers in the interval [1, X]. With a O(X) auxiliar array and a flag we can do this in constant time, and the
# answer is the last index achieved when we fill the aux arr.


def solution(arr, j, x):
    # this is a greedy algorithm that makes the fastest jump possible, regardless the distance of the jump
    # we won't leave a fastest path nor reach a dead end, because when we "jump" we always expand forward
    # the leaves that are reachable
    actual = 0 # start from position 0
    time = -1 # at the start of the algorithm we didn't move
    adv = True # if in a loop we can't advance and didn't reach x, then there's no solution
    while actual < x and adv:
        adv = False
        for i in range(len(arr)):
            elem = arr[i]
            if elem > actual and elem <= (actual+j): # we search for the first reachable (<= actual+j) leaf that moves us forward (> actual)
                actual = elem
                time = max(i, time)
                adv = True
                break

    return time if actual >= x else -1

def main():
    x = int(sys.argv[1])
    j = int(sys.argv[2])
    arr = list(map(int, sys.argv[3:]))

    r = solution(arr, j, x)

    print(r)
    return r

if __name__ == "__main__":
    main()