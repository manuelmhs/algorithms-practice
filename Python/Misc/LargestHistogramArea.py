"""
Largest Rectangular Area in a Histogram

Given a histogram represented by an array arr[], where each element of the array denotes the height of the bars in the histogram.
All bars have the same width of 1 unit.
Task is to find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of
contiguous bars whose heights are given in an array.

Input: arr[] = [60, 20, 50, 40, 10, 50, 60]
Output: 100
We get the maximum by picking the bars 50 and 60.
The area is computed (smallest height) * (no. of the picked bars) = 50 * 2 = 100.
"""

import sys
from Python.Arrays.NearestNumbers import NearestNumbers

# the idea: we iter through all the array. In each step, we consider arr[i] as the min height to form a rectangle
# which we try to expand the maximum possible to each sides. Like this, at the end of the loop, we will have considered
# the best possible rectangle for each height present in the array. The best rectangle overall is the maximum of these.
# A more intuitive idea would be using two nested loop to consider all possible rectangles in the array.
# Time complexity: O(n^2), Space complexity: O(1)
def naive(arr):
    l = len(arr)
    best = -1
    for i in range(l):
        minH = arr[i]
        
        j = i+1
        while j < l and arr[j] >= minH:
            j += 1

        k = i-1
        while k >= 0 and arr[k] >= minH:
            k -= 1
        
        rect = (j - (k+1)) * minH
        best = max(rect, best)

    return best

# this is a improvement of the naive idea: we just use a more efficient way to detect where to stop the rectangle,
# without needing to iterate to the left and right for each element. Instead, we use the left/right nearest smaller numbers
# algorithm, that calculates in O(n) time where is the nearest smaller value to the left or right of all the elements of the array
# Time Complexity: O(n), Space Complexity: O(n)
def precomputingNearestValues(arr):
    # we precompute the necessary information
    leftSmaller = NearestNumbers(arr, 1, 0)
    rightSmaller = NearestNumbers(arr, -1, 0)

    l = len(arr)
    best = -1
    for i in range(l):
        # for each element in the array, we calculate in O(1) the corresponding area and actualize the best area
        height = arr[i]

        leftBoundary = leftSmaller[i] + 1
        rightBoundary = rightSmaller[i]

        temp = height * (rightBoundary - leftBoundary)
        best = max(best, temp)

    return best

def main():
    arr = list(map(int, sys.argv[1:]))

    r = precomputingNearestValues(arr)

    print(r)
    return r


if __name__ == "__main__":
    main()