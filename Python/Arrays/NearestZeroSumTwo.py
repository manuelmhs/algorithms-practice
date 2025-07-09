"""
Given a list of Int (positive or negative), find the (x,y) pair of numbers which sum (x+y) is nearest to 0.
Assume there's at least 2 numbers in the list.
"""

import sys

# Naive implementation, iterating through all possible pairs
# Time complexity: O(n^2) (the number of all possible pairs)
def aux(t1,t2):
    a,b = t1
    x,y = t2
    if abs(a+b) <= abs(x+y):
        return t1
    else:
        return t2
    
def naive(list):
    a = list[0]
    b = list[1]

    for i, n in enumerate(list[:len(list)-1]):
        a,b = aux((a,b), (n,list[i+1]))

        if a+b == 0:
            break
        
        for m in list[i+2:]:
            a,b = aux((a,b), (n,m))
    
    return (a,b)

# Sorting + Two-pointer algorithm
# the idea is to first sort the array in ascending order, then, using two pointers (one from each side of the array)
# calculate the sum (update the closest sum if necessary), and follow: if the current sum is negative,
# move the left pointer one step to the right. Otherwise, move right pointer one step to the left
# Time complexity: O(n*lg n) (O(n*lg n) because of sorting algorithm, + O(n) because of iteration through array)
def ClosestZeroSumTwo(arr : list[int]):
    # assume that sorting algorithm is O(n*lg n)
    arr.sort()

    closest = (float("inf"), 0, 0) # leave (closestSum, x, y) to return (x,y) pair
    leftPtr = 0
    rightPtr = len(arr)-1

    while leftPtr < rightPtr: # we iterate until both pointers are equal, so we iterate through all the array (worst case)
        left = arr[leftPtr]
        right = arr[rightPtr]
        tempSum = left + right
        sumAbs = abs(tempSum)

        if sumAbs == 0:
            return (left, right)

        if sumAbs <= closest[0]:
            closest = (sumAbs, left, right)
        
        if tempSum < 0:
            leftPtr += 1
        else:
            rightPtr -= 1

    return (closest[1], closest[2])

def main():
    arr = list(map(int, sys.argv[1:]))

    a, b = ClosestZeroSumTwo(arr)

    print(f"({a},{b})")
    return (a,b)

if __name__ == "__main__":
    main()