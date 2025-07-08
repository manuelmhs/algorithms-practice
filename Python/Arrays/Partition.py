"""
Given an array arr[], partition it by it's first element, in two subsets: all lower-equal elements, and greater elements.
if arr = [3,4,1,2,5] -> [2,1] or [1,2] + [3] + [4,5] or [5,4]
Note: this partition algorithm must be in place. It's useful to implement a Quick Sort algorithm.
"""

import sys

# not in place implementation
# Time complexity: O(n), Auxiliar space: O(n)
def naive(arr):
    if len(arr) == 0:
        return

    # generates two arrays, dropping each arr's element in the corresponding one, then writes back to arr
    pivot = arr[0]
    lowEq = []
    gre = []

    for i in range(1, len(arr)):
        n = arr[i]
        if n <= pivot:
            lowEq.append(n)
        else:
            gre.append(n)

    for i in range(len(arr)):
        if i < len(lowEq): # reads lower-equal elements
            arr[i] = lowEq[i]
        elif i == len(lowEq): # pivot element
            arr[i] = pivot
        else: # greater elements
            arr[i] = gre[i-len(lowEq)-1] # offset

# Time complexity: ¿O(n^2)?, Auxiliar space: O(1)
def naiveInPlace(arr):
    # we loop through the array, leaving greater values in place (because they are after the pivot)
    # if we encounter a lower-equal value, we copy it to the pivot's position and
    # we push the subarray between the pivot (included) and this value, one space forward
    # e.g if 5 == pivot and we are comparing with 2: [5, 11, 7, 2] -> [2, 5, 11, 7]
    pivotIdx = 0

    for i in range(1, len(arr)):
        n = arr[i]
        pivot = arr[pivotIdx]
        if n <= pivot:
            carry = pivot
            arr[pivotIdx] = arr[i]
            pushes = i - pivotIdx

            for j in range(pushes): # the problem with this implementation is the inner loop
                temp = arr[pivotIdx+j+1]
                arr[pivotIdx+j+1] = carry
                carry = temp

            pivotIdx += 1
        else:
            continue

# Time complexity: O(n), Auxiliar space: O(1)
def Lomuto(arr, pivotIdx=0):
    # Lomuto is a in-place, O(n) time complexity partition algorithm
    # the default pivot is the last element. we loop through the array, marking the last element that is lower-equal to the pivot (boundary)
    # if we encounter a greater value, we just continue
    # otherwise, if lower-equal value, we swap it with the immediate next element to the boundary, and increment boundary by 1
    # finally, the pivot will swap places just outside the boundary, leaving all lower-equal elements to the left, and greater to the right
    # it's more efficient than naives algorithms, but unlike them it's not a stable algorithm

    if len(arr) == 0:
        return

    # we can choose which element is the pivot by swapping it with the last element
    temp = arr[pivotIdx]
    arr[pivotIdx] = arr[-1]
    arr[-1] = temp

    pivot = arr[-1]
    j = 0 # boundary index
    for i in range(len(arr)):
        n = arr[i]
        if n <= pivot: # because pivot will satisfy this if statement,  we don't need a special case
            arr[i] = arr[j] # swap actual element with boundary index
            arr[j] = n
            j += 1 # expand boundary
        else:
            continue

def main():
    arr = list(map(int, sys.argv[1:]))

    arr1 = arr[:]
    arr2 = arr[:]
    arr3 = arr[:]

    naive(arr1)
    naiveInPlace(arr2)
    Lomuto(arr3)

    print(arr1)
    print(arr2)
    print(arr3)
    return (arr1, arr2, arr3)

if __name__ == "__main__":
    main()