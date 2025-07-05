"""
Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
Could you come up with a one-pass algorithm using only constant extra space?
"""

import sys

def main():
    arr = list(map(int, sys.argv[1:]))
    
    #we use an indexes to point to the first appearance of a 1 or 2 digit
    firstOneIdx = -1
    firstTwoIdx = -1
    for i, bin in enumerate(arr):
        if bin == 0: #can change positions if there's a 1 or 2 digit before in the list
            if firstOneIdx != -1: #we change with the 1 digit
                arr[firstOneIdx] = 0
                arr[i] = 1
                
                bin = 1 #we set the actual digit to 1, in case there's also a 2 digit before i
                firstOneIdx += 1
                if firstTwoIdx == firstOneIdx: #careful with the index in this case
                    firstOneIdx = -1
            elif firstTwoIdx != -1: #we simply swap with the 2 digit
                arr[firstTwoIdx] = 0
                arr[i] = 2
                firstTwoIdx += 1 #important: the second 2 digit is always next to the first one (maybe == i or not)
        if bin == 1: #can change positions if there's a 2 digit before in the list
            if firstTwoIdx != -1:
                #swap positions
                arr[firstTwoIdx] = 1
                arr[i] = 2
                firstTwoIdx += 1 #important

                if firstOneIdx == -1:
                    firstOneIdx = firstTwoIdx - 1
            
            elif firstOneIdx == -1:
                firstOneIdx = i
        if bin == 2: #simply check if index must be initialized
            if firstTwoIdx == -1:
                firstTwoIdx = i

    print(arr)
    return arr

if __name__ == "__main__":
    main()