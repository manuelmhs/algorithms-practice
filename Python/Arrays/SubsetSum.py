from Python.Arrays.AllSubsets import iterative as AllSS

"""
Given an array arr[] of integers and a value sum, the task is to check if there is a subset of the given array whose sum
is equal to the given sum.

Assume arr[] is non-empty.
"""

# given that numbers can be negative, we can not prune branches if we "overshoot" the target sum

import sys

# direct implementation with AllSubsets function
# Time = Space: O(2^n)
def FromAllSubsets(arr, targetSum):
    subsets = AllSS(arr)
    subsets.remove([]) # we can exclude/include empty set if we want/don't want to trivially sum 0

    finish = False
    i = 0
    while not finish and i < len(subsets):
        s = sum(subsets[i])
        if s == targetSum:
            finish = True
        else:
            i += 1

    return finish

# Time: O(2^n), Space: O(n) (if we don't copy arr in each recursion call, just for the stack size)
def naive(arr, targetSum):
    # this implementation considers that targetSum = 0 is always possible (empty set)
    l = len(arr)

    if targetSum == 0:
        return True
    elif (l == 0):
        return False
    else:
        # in case arr[] is only conformed of positive numbers, we could exclude elem if elem > targetSum
        elem = arr[0]
        return naive(arr[1:], targetSum-elem) or naive(arr[1:], targetSum)
    
# non-negative numbers only
# this is a memoization improvement over the naive implementation
# problem is the lookup table can become really (and unnecessarily) large if we work with big values
# Time = Space: O(n*targetSum)
def ClassicMemo(arr, targetSum, n = -1, memo = None):
    # we use a memo or lookup table of size (n+1)*(targetSum+1)
    # an entry memo[i][k] stores True if it's possible to sum k with any subset within [0, i] elements, False otherwise
    # note: we have n+1 rows because memo[0] is reserved to the empty set,
    # and have targetSum+1 columns because we consider the [0, targetSum] values (including both ends)
    if n == -1 and memo == None:
        n = len(arr)
        # careful with: [[-1] * (targetSum+1)] * (n+1). this just generates once the inner list and all rows
        # end up referencing to it
        memo = [[-1] * (targetSum+1) for _ in range(n+1)]

    # base cases
    if targetSum == 0:
        return True
    elif n == 0:
        return False
    
    # we first in the lookup table to avoid repetitive calculations
    if memo[n][targetSum] != -1:
        return memo[n][targetSum]

    elem = arr[n-1]
    if elem > targetSum: # exclude current elem (otherwise targetSum - elem is out of index access in memo)
        memo[n][targetSum] = ClassicMemo(arr, targetSum, n-1, memo)
    else: # consider including or not elem, in both cases recursion with n-1 elements
        memo[n][targetSum] = ClassicMemo(arr, targetSum - elem, n-1, memo) or ClassicMemo(arr, targetSum, n-1, memo)

    return memo[n][targetSum]

# non-negative numbers only
# exact same idea as ClassicMemo, just it's bottom-up iterative tabulation
# will probably make much more unnecessary calculations as it fills all entries in the lookup table
# anyways the worst case scenario is the same
# Time = Space: O(n*targetSum)
def ClassicTabulation(arr, targetSum):
    n = len(arr)
    dp = [[False] * (targetSum+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True # for any number of values it's always possible to sum 0

    # the first row will always be [True, False, False, ...] because the empty set only sums 0
    for i in range(1, n+1):
        elem = arr[i-1]
        for sum in range(1, targetSum+1):
            if elem > sum:
                dp[i][sum] = dp[i-1][sum]
            else:
                # the trick is that we don't need to check if dp[j][k] is calculated or not
                # nor do recursion because we linearly fill all entries, and dp[i-1][sum-elem] only goes back to
                # a calculated value
                dp[i][sum] = dp[i-1][sum] or dp[i-1][sum-elem]

    return dp[n][targetSum]
    
# the previous implementation leads to this optimization: within the inner loop, we only access dp[i-1][sum] or dp[i-1][sum-elem]
# to set dp[i][sum], this is, we only need to save in memory the previous and the current row
# Time: O(n*targetSum), Space: O(targetSum)
def SpaceOptimizedTabulation(arr, targetSum):
    n = len(arr)
    previousRow = [True if s == 0 else False for s in range(targetSum+1)]

    for i in range(1, n+1):
        elem = arr[i-1]
        currentRow = [True if s == 0 else False for s in range(targetSum+1)]
        for s in range(1, targetSum+1):
            if elem > s:
                currentRow[s] = previousRow[s]
            else:
                currentRow[s] = previousRow[s] or previousRow[s-elem]

        previousRow = currentRow
    
    return currentRow[targetSum]

# tabulation
def iterative(arr, targetSum):
    finish = False
    # we use a set to avoid repetition of partial sums (e.g in [2,3,5] 2+3 == 5)
    sums = set()
    for i, n in enumerate(arr):
        # we do not generate a copy each time, so we don't need to insert old elements again

        # add new possible sums to sums
        newElements = set()
        for m in sums:
            newElements.add(n+m)
        sums.update(newElements)

        # add actual element
        sums.add(n)

        if targetSum in sums: # could check in each sum to stop earlier if possible, also to not check again in old values
            finish = True
            break

    return finish

# memoization
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

def main():
    arr = list(map(int, sys.argv[1:len(sys.argv)-1]))
    targetSum = int(sys.argv[len(sys.argv)-1])

    (r1, _) = recursive(arr, targetSum)
    r2 = iterative(arr, targetSum)
    r3 = FromAllSubsets(arr, targetSum)

    print(r1, r2, r3,)
    return (r1, r2, r3)

if __name__ == "__main__":
    main()