import sys

# idea: we leave at the left of the array the sorted portion, and step by step select the minimum value in the unsorted portion
# then we swap places with the element at the right of the sorted portion and repeat until all array is sorted

def SelectionSort(arr):
    l = len(arr)
    for i in range(l):
        minimumIdx = i
        for j in range(i+1, l):
            if arr[j] < arr[minimumIdx]:
                minimumIdx = j

        temp = arr[i]
        arr[i] = arr[minimumIdx]
        arr[minimumIdx] = temp

def main():
    arr = list(map(int, sys.argv[1:]))

    SelectionSort(arr)

    print(arr)
    return arr

if __name__ == "__main__":
    main()