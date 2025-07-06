import sys
from math import floor

# the idea of merge sort: this a top-down, divide and conquer algorithm, we start from the whole array, and in each step
# we split in halves (divide). then we recursively sort the corresponding halves (recursion) and finally sort the resulting halves (merge)
# the important thing is that we know that each half will be sorted properly due to recursion

#we modify the original arr instead of creating a new one in each recursion for optimization
def MergeSort(arr, start=-1, end=-1):
    if (start == end == -1):
        start = 0
        end = len(arr)

    l = end - start

    if (l == 0): #shouldn't happen if arr isn't initially []
        #return []
        return None
    if (l == 1):
        #return arr
        return None
    else:
        #split
        mid = floor(l / 2) + start

        #recursion
        #left = MergeSort(arr, start, mid)
        #right = MergeSort(arr, mid, l)
        MergeSort(arr, start, mid)
        MergeSort(arr, mid, end)

        #merge
        ordered = [None] * l #we buffer the ordered merged list
        idxLeft = start
        idxRight = mid
        for i in range(l):
            #if one list is empty, we take elements directly from the other one
            if (idxLeft >= mid):
                ordered[i] = arr[idxRight]
                idxRight += 1
            elif (idxRight >= end):
                ordered[i] = arr[idxLeft]
                idxLeft += 1
            #otherwise, we check for order
            elif (arr[idxLeft] <= arr[idxRight]):
                ordered[i] = arr[idxLeft]
                idxLeft += 1
            else:
                ordered[i] = arr[idxRight]
                idxRight += 1
        #we write the ordered list
        for i in range(l):
            arr[start + i] = ordered[i]

        #return arr
        return None

def main():
    arr = list(map(int, sys.argv[1:]))
    
    MergeSort(arr)

    print(arr)
    return arr

if __name__ == "__main__":
    main()