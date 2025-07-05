"""
You are given a binary array arr[], where each element is either 0 or 1.
Your task is to rearrange the array in increasing order in place (without using extra space).
You do not need to return anything; simply modify the input array.
"""

import sys

def main():
    arr = list(map(int, sys.argv[1:]))

    countZeroes = 0

    for bin in arr:
        if bin == 0:
            countZeroes += 1

    for i in range(len(arr)):
        if countZeroes > 0:
            arr[i] = 0
            countZeroes -= 1
        else:
            arr[i] = 1

    print(arr)
    return arr

if __name__ == "__main__":
    main()