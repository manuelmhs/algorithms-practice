import sys

# idea: instead of leaving the maximum values at the end like bubble sort, we leave the minimum values at the beginning
# we start sorting the first element of the array (it already is sorted itself), then go on to the second element, and so on
# we push the greater elements forward (from the sorted part) until the element we intend to insert is no longer smaller,
# reading the sorted part from right to left

def InsertionSort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j =  i-1
        stop = False

        while j >= 0 and not stop:
            if val < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            else:
                stop = True

        arr[j+1] = val

def main():
    arr = list(map(int, sys.argv[1:]))

    InsertionSort(arr)

    print(arr)
    return arr

if __name__ == "__main__":
    main()