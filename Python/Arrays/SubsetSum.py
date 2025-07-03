from Python.Arrays.AllSubsets import iterative as AllSS

"""
Given an array arr[] of integers and a value sum, the task is to check if there is a subset of the given array whose sum
is equal to the given sum.
"""

# given that numbers can be negative, we can not prune branches if we "overshoot" the target sum

import sys

def FromAllSubsets(arr, targetSum):
    subsets = AllSS(arr)
    subsets.remove([])

    finish = False
    i = 0
    while not finish and i < len(subsets):
        s = sum(subsets[i])
        if s == targetSum:
            finish = True
        else:
            i += 1

    return finish

#memoization

def recursive(arr, targetSum):
    l = len(arr)
    elem = arr[0]

    if (l == 1):
        if elem == targetSum:
            return (True, set([elem]))
        else:
            return (False, set([elem]))
    else:
        if elem == targetSum:
            return (True, set([elem]))
        else:
            (flag, sums) = recursive(arr[1:], targetSum)
            if flag:
                return (True, set([targetSum]))
            else:
                newElements = set()
                for s in sums:
                    newElem = s+elem

                    if (newElem == targetSum):
                        return (True, set([newElem]))
                    
                    newElements.add(newElem)

                sums.update(newElements)
                sums.add(elem)

                return (False, sums)

#usage of DP and avoid of repetitions

def iterative(arr, targetSum):
    finish = False
    #we use a set to avoid repetition of partial sums (e.g in [2,3,5] 2+3 == 5)
    sums = set()
    for i, n in enumerate(arr):
        #we do not generate a copy each time, so we don't need to insert old elements again

        #add new possible sums to sums
        newElements = set()
        for m in sums:
            newElements.add(n+m)
        sums.update(newElements)

        #add actual element
        sums.add(n)

        if targetSum in sums: #could check in each sum to stop earlier if possible, also to not check again in old values
            finish = True
            break

    return finish

def main():
    arr = list(map(int, sys.argv[1:len(sys.argv)-1]))
    targetSum = int(sys.argv[len(sys.argv)-1])

    (r1, _) = recursive(arr, targetSum)
    r2 = iterative(arr, targetSum)
    r3 = FromAllSubsets(arr, targetSum)

    print(r1, r2, r3)
    return (r1, r2, r3)

if __name__ == "__main__":
    main()