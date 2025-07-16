"""
------ Staircase: ------
There are n stairs, a person standing at the bottom wants to reach the top.
The person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top.
"""

import sys

# the problem is solved with the following logic: we can reach a given stair n by a 1-long step from n-1,
# and a 2-long step from n-2. So, the number of ways to reach stair n is the sum of ways to reach n-1 and ways to reach n-2
# this is a disjoint sum because the last step is different, and no option is left out
def staircase(n, memo=None):
    if not memo:
        memo = {}
    # we consider the base cases as follows: n == 0 (the stair doesn't exist), n == 1 (one option, don't do anything)
    # and n == 2 (one option, move 1)
    if n <= 2:
        memo[n] = 1
    else:
        if n not in memo:
            memo[n] = staircase(n-1, memo) + staircase(n-2, memo)
    
    return memo[n]

def main():
    n = int(sys.argv[1])
    r = staircase(n)

    print(r)
    return r

if __name__ == "__main__":
    main()