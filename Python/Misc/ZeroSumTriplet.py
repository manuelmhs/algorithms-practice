"""
Given an array arr[] of integers, determine whether it contains a triplet whose sum equals zero.
Return true if such a triplet exists, otherwise, return false.

Input: arr[] = [0, -1, 2, -3, 1]
Output: true

Input: arr[] = [1, 2, 3]
Output: false
"""

import sys

# Time complexity: O(n^3), Space complexity: O(1)
def naive(arr):
    l = len(arr)
    flag = False
    i = 0
    while i < l-2 and not flag:
        j = i+1
        while j < l-1 and not flag:
            k = j+1
            while k < l and not flag:
                if arr[i] + arr[j] + arr[k] == 0:
                    flag = True
                k += 1
            j += 1
        i += 1

    return flag

# Time complexity: O(n^2), Space complexity: O(n)
# we use a hash table (in this case a set) to save the indexes we already passed as "i" indexes. We just need to use
# two loops to iterate through all possible pairs, with j and k indexes, searching for a pair that sums 0 with any previous i index.
# the idea comes from: we search for i, j, k indexes such that arr_i + arr_j + arr_k == 0 -> arr_i = - (arr_j + arr_k), i.e. if the
# complement of arr_j + arr_k is in the set, that's a valid triplet that sums 0
def hashmapOptimization(arr):
    l = len(arr)
    i_s = set()
    for j in range(l-1): # we only need two loops
        for k in range(j+1, l):
            target = -(arr[j] + arr[k])

            if target in i_s:
                return True
        
        # when we finished using j index, we add it as a i index to the hashmap, not earlier
        # this is because we need a triplet such that i < j < k, i = j < k wouldn't be a correct answer
        if not arr[j] in i_s: 
            i_s.add(arr[j])

    return False

# Time complexity: O(n^2), Space complexity: O(1)
# idea: use the algorithm of Nearest Zero Sum Two, that uses two pointers to achieve the closest sum possible of a pair to 0
# in this case, we first sort the array, then set a a_i number, and try to sum -a_i using two pointers, with the rest of the
# elements of the array
def twoPointersOptimization(arr):
    arr.sort()
    l = len(arr)
    for i in range(l):
        target = -arr[i]
        leftPtr = 0
        rightPtr = l-1
        while leftPtr < rightPtr:
            # careful not to consider arr[i] as a part of the triplet
            if leftPtr == i:
                leftPtr += 1
            elif rightPtr == i:
                rightPtr -= 1
            else:
                s = arr[leftPtr] + arr[rightPtr]
                if s == target:
                    return True
                elif s < target:
                    leftPtr += 1
                else:
                    rightPtr -= 1
    
    return False

def main():
    arr = list(map(int, sys.argv[1:]))

    r = twoPointersOptimization(arr)

    print(r)
    return r

if __name__ == "__main__":
    main()