"""
Given an array arr[] of n sorted linked lists of different sizes. The task is to merge them in such a way that after merging
they will be a single sorted linked list, then return the head of the merged linked list.

Input: arr[] = [1 -> 2 -> 3, 4 -> 5, 5 -> 6, 7 -> 8]
Output: 1 -> 2 -> 3 -> 4 -> 5 -> 5 -> 6 -> 7 -> 8

Input: arr[] = [1 -> 3, 8, 4 -> 5 -> 6]
Output: 1 -> 3 -> 4 -> 5 -> 6 -> 8
"""

import sys

# could be optimized using divide and conquer or min heap approaches
# min heap would make n iterations of cost lg k -> n*lg k
# divide and conquer would generate a (lg k)-height recursion binary tree and in each floor we have cost n to sort
# -> n*lg k again

# we represent linked lists as python arrays for convenience (will use them as lists)
# Time complexity: O(n*k), where n is the total number of elements and k the number of lists
# we iterate n times, retrieving one element at a time, making k comparisons (to select the min one from k lists)
def MergeLists(listsArr : list[list[int]]):
    finalList = []

    # we use a hashmap (set in this case) to save all listsArr lists's indexes with elements left
    # this is costly to initialize, but then it grants us O(1) time deletes
    # could remove the empty list directly from listsArr, but that operation has O(n) time cost
    indexes = set()
    [indexes.add(i) for i in range(len(listsArr))]

    # we iterate as long we have at least 1 non-empty list
    l = len(indexes)
    while l > 0:
        minVal = float("inf")
        minIdx = -1
        for i in indexes: # we search the min, first value through all non-empty lists
            if listsArr[i][0] < minVal:
                minVal = listsArr[i][0]
                minIdx = i

        finalList.append(minVal) # append it to the resultant list
        # pop it from the original list and remove it's index from the hashmap if it has no more values
        listsArr[minIdx].pop(0)
        if len(listsArr[minIdx]) == 0:
            indexes.remove(minIdx)
            l -= 1

    # because we access to both ends of our "lists", a singly linked list with references to both ends would do a good job

    return finalList

def main():
    listsArr = []
    temp = []
    for e in sys.argv[1:]:
        if e != "b":
            temp.append(int(e))
        else:
            listsArr.append(temp)
            temp = []
    if temp:
        listsArr.append(temp)

    merged = MergeLists(listsArr)

    print(merged)
    return merged

if __name__ == "__main__":
    main()