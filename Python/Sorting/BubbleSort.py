import sys

# the idea of bubble sort: we loop through the array n times, carrying the largest element to the last non-definitive position
# in the first iteration, the largest element lands on the last position. in the second iteration, the second largest element
# lands on the second to last position, and so on

# W(n) = S(n) = n^2
def BubbleSort(arr):
    l = len(arr)

    for i in range (l):
        for j in range (l - i):
            if j > 0 and arr[j-1] > arr[j]: #shorcircuited and to avoid out of index access
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp

def BubbleSortOptimization(arr):
    l = len(arr)

    #we check for the last element modified in each inner loop: if no element was modified, the array is sorted
    #if the last element modified was of index k, in the next inner loop we only reach up to that index
    last = l
    for i in range (l):
        tempLast = 0
        for j in range (l - i):
            if j >= last:
                break
            
            if j > 0 and arr[j-1] > arr[j]:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp

                tempLast = j
            
        if tempLast == 0:
            break
        else:
            last = tempLast

def main():
    arr = list(map(int, sys.argv[1:]))
    
    BubbleSortOptimization(arr)

    print(arr)
    return arr

if __name__ == "__main__":
    main()