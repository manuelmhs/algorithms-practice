import sys

# idea: we choose a element of our array to be the pivot, and then partition the array in two halves, lower (or equal) and higher values (divide)
# then we recursively sort the two halves (recursion) and finally merge the solution (merge)
# difference with merge sort, in this case merging is trivial and the split is costful

# naive, functional implementation
def naive(arr):
    l = len(arr)
    if l == 0:
        return []
    elif l == 1:
        return [arr[0]]
    else:
        #split
        #arbitrarily select first element as pivot
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, l):
            if arr[i] <= pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        #recursion
        left = naive(left)
        right = naive(right)
        #merge
        return left + [pivot] + right


from Python.Arrays.Partition import Lomuto
from random import randint

def QuickSort(arr, start=-1, end=-1): # better not use None as default because it's falsy as 0 (which is a valid index)
    # if not start and not end: CAREFUL FOR start = end = 0
    if start == end == -1:
        start = 0
        end = len(arr)

    l = end - start
    if l <= 1: # base case
        # trivial, doesn't do anything
        return
    else: # recursive case
        # split
        pivotIdx = randint(start, end-1)
        k = Lomuto(arr, pivotIdx, start, end)
        # recursion
        QuickSort(arr, start, k)
        QuickSort(arr, k+1, end)

        # merge
        # in this algorithm merge is trivial

def main():
    arr = list(map(int, sys.argv[1:]))

    QuickSort(arr)

    print(arr)
    return arr

if __name__ == "__main__":
    main()