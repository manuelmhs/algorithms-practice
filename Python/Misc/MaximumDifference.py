"""
Given an integer array arr of integers, the task is to find the maximum absolute difference between the nearest left smaller
element and the nearest right smaller element of every element in array arr. If for any component of the arr, the nearest smaller
element doesn't exist then consider it as 0.

Input: arr = [2, 1, 8]
Output: 1

Input: arr = [2, 4, 8, 7, 7, 9, 3]
Output: 4
"""

import sys

# precalculate nearest left/right smaller numbers to each element in O(n) using the stack approach
def nearestSmaller(arr, dir = 1):
    stack = []
    ns = [0] * len(arr)

    start = 0
    end = len(arr)
    step = 1
    if dir == -1:
        start = len(arr)-1
        end = -1
        step = -1

    for i in range(start, end, step):
        elem = arr[i]
        while stack and stack[-1] >= elem:
            stack.pop()
        
        if stack:
            ns[i] = stack[-1]

        stack.append(elem)

    return ns

# first we calculate neareast left and right smaller numbers for each element in O(n)
# then, we just have to iterate through this lists calculating the max abs difference between same index elements
# Time complexity = Auxiliar space: O(n)
def solution(arr):
    nls = nearestSmaller(arr, 1)
    nrs = nearestSmaller(arr, -1)

    maximum = float("-inf")
    for i in range(len(arr)):
        maximum = max(maximum, abs(nls[i]-nrs[i]))

    return maximum

def main():
    arr = list(map(int, sys.argv[1:]))

    r = solution(arr)

    print(r)
    return r

if __name__ == "__main__":
    main()