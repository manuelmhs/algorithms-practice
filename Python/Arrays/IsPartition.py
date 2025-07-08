"""
Given two arrays, p[] and arr[], check if p[] is partition of arr[] (partitioned by the first element), returning True of False appropiately.
p[] is partition of arr[] if:
- it contains exactly the same elements
- if arr's first element is pivot, then p = [p_0, p_1, ..., p_pivot-1, pivot, p_pivot+1, ..., p_pivot+n],
  where p_i <= pivot if i <= pivot-1, and p_ì >= pivot if i >= pivot+1
"""

import sys

# Time complexity: O(n+m), Space complexity: O(n), where n = len(p), m = len(arr)
def IsPartition(p, arr):
    # check if lengths are equal, check if arrays are empty
    l1 = len(p)
    l2 = len(arr)

    if l1 != l2:
        return False
    elif l1 == 0:
        return True
    
    # we use a dictionary to register the number of times each element appears in p
    # then, we check if the exact same of apparitions happens in arr
    dic = dict()

    pivot = arr[0]
    # we need this information to know if the partitions order is correct (if there couldn't be any duplicates it would be much easier)
    lastLowerIdx = -1
    firstGreaterIdx = len(p)
    pivotIdxs = []
    for i, n in enumerate(p):
        # we update the necessary indexes to check if order is correct
        if n < pivot:
            lastLowerIdx = i
        elif n == pivot:
            pivotIdxs.append(i)
        elif n > pivot and firstGreaterIdx == len(p):
            firstGreaterIdx = i
            
        # checking occurrences
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1

    # we need a pivot index that confirms: all lower values are to the left (this is, the last lower value is to the left)
    # and at the same time, all greater values are to the right (this is, the first greater value is to the right)
    # if at least one pivot is valid, then the partition order is correct
    validOrder = False
    for pivotIdx in pivotIdxs:
        if pivotIdx > lastLowerIdx and pivotIdx < firstGreaterIdx:
            validOrder = True
            break

    if not validOrder:
        return False
    
    # check if p occurrences match with arrs occurrences
    for m in arr:
        if m in dic:
            dic[m] -= 1
        else:
            return False
        
    for v in dic.values():
        if v != 0:
            return False
        
    return True

def main(p = None, arr = None):
    if not p and not arr:
        p = []
        arr = []
        pointer = p
        for i in range(1, len(sys.argv)):
            if sys.argv[i] == "continue":
                pointer = arr
                continue

            pointer.append(sys.argv[i])
    
    flag = IsPartition(p, arr)

    print(flag)
    return flag

if __name__ == "__main__":
    main()