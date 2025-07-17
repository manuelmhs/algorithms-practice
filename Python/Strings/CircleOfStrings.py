"""
Given an array arr of lowercase strings, determine if the strings can be chained together to form a circle.
A string X can be chained together with another string Y if the last character of X is the same as the first
character of Y. If every string of the array can be chained with exactly two strings of the array
(one with the first character and the second with the last character of the string), it will form a circle.

For example, for the array arr[] = {"for", "geek", "rig", "kaf"} the answer will be Yes as the given strings
can be chained as "for", "rig", "geek" and "kaf"

Input: arr[] = ["abc", "bcd", "cdf"]
Output: 0

Input: arr[] = ["ab" , "bc", "cd", "da"]
Output: 1
"""

# this problem must (or should) be solved using graph theory: creating a directed graph where the first and last letters of our strings
# are the nodes, connected by a directed edge (if we have "abc", then a and c are nodes, with a directed edge from a to c)
# then we have to prove there's a eulerian circuit in that directed graph

import sys

# this is a naive, not fully functional implementation, because it doesn't checks connectivity
# we try to match first with lasts characters and check there's no character left out. But we may pass as a valid answer
# two different circles, like ab bc ca de ef fd. It only works with simple cases
def circleStrings(arr):
    l = len(arr)
    chains = [(-1, -1)] * l # we try to "chain" first and last characters with corresponding ones from other words

    for i in range(l):
        currStr = arr[i]
        leftChain, rightChain = chains[i]

        # we use an inner loop, leading to O(n^2) complexity. This could be solved iterating through the array first, saving
        # relevant chars in a hashmap. This would get rid of this inner loop and end with a constant time operation
        for j in range(i+1, l):
            otherStr = arr[j]
            otherLeft, otherRight = chains[j]

            if leftChain == otherRight == -1 and currStr[0] == otherStr[-1]:
                leftChain = j
                otherRight = i
            elif rightChain == otherLeft == -1 and currStr[-1] == otherStr[0]:
                rightChain = j
                otherLeft = i

            chains[i] = (leftChain, rightChain)
            chains[j] = (otherLeft, otherRight)
        
        if chains[i][0] == -1 or chains[i][1] == -1:
            return False
        
    return True

def main():
    arr = sys.argv[1:]

    r = circleStrings(arr)

    print(r)
    return r

if __name__ == "__main__":
    main()