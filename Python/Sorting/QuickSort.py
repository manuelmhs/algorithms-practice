import sys

# idea: we choose a element of our array to be the pivot, and then partition the array in two halves, lower (or equal) and higher values (divide)
# then we recursively sort the two halves (recursion) and finally merge the solution (merge)
# difference with merge sort, in this case merging is trivial and the split is costful

# naive, functional implementation
def QuickSort(arr):
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
        left = QuickSort(left)
        right = QuickSort(right)
        #merge
        return left + [pivot] + right

def main():
    arr = list(map(int, sys.argv[1:]))

    arr = QuickSort(arr)

    print(arr)
    return arr

if __name__ == "__main__":
    main()