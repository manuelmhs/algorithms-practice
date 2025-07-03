"""
Given an array arr[], rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer.
Do the mentioned change in the array in place.
Note: consider the array as circular
"""

import sys
from collections import deque

def main():
    arr = list(map(int, sys.argv[1:-1]))
    d = int(sys.argv[-1])

    l = len(arr)
    d = d % l
    q = deque()

    if d > 0:
        for i in range(l+d):
            if (i < d): #fill queue
                if i == 0:
                    q.append(arr[i])
                else:
                    q.append(arr[l-i]) #this is equivalent to arr[-i], except in case i == 0
            elif (d <= i < l): #write and refill
                q.append(arr[l-i])
                arr[l-i] = q.popleft()
            else: #only write
                j = i % l
                if j == 0:
                    arr[j] = q.popleft()
                else:
                    arr[l-j] = q.popleft()
    
    print(arr)
    return arr

if __name__ == "__main__":
    main()