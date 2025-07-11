"""
Generalization of Left Nearest Smaller Numbers: supports looking for left/right nearest smaller/greater numbers.
Returns the indexes of the values, not the values itself.
"""

import sys
from collections import deque

def NearestNumbers(arr, direction=1, comparison=0):
    """Set direction = 1 to search for left nearest, direction = -1 to search for right nearest.
    
    Set comparison = 0 to search for smaller numbers, comparison = 1 to search for greater numbers."""

    l = len(arr)
    result = [None] * l
    q = deque()

    start = end = -1
    if direction == 1:
        start = 0
        end = l
    elif direction == -1:
        start = l-1
        end = -1

    compare = None
    if comparison == 0:
        compare = lambda x,y: x < y
    elif comparison == 1:
        compare = lambda x,y: x > y

    for i in range(start, end, direction):
        n = arr[i]

        while len(q) > 0 and compare(n, q[0][0]):
            q.popleft()
        
        nearestIdx = -1 if direction == 1 else l
        if len(q) > 0:
            nearestIdx = q[0][1]

        result[i] = nearestIdx
        q.appendleft((n, i))

    return result

def main():
    arr = list(map(int, sys.argv[1:]))

    r = NearestNumbers(arr)

    print(r)
    return r

if __name__ == "__main__":
    main()