"""
Implementation of Fibonacci using recursion + memoization.
"""

import sys

calls = 0

#W(n) = 2^n, S(n) = n
def FibStandard(n):
    global calls
    calls += 1

    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return FibStandard(n-1) + FibStandard(n-2)

#W(n) = S(n) = n
def FibTupling(n):
    global calls
    calls += 1

    if (n == 0):
        return (0, -1)
    elif (n == 1):
        return (1, 0)
    else:
        f_n1, f_n2 = FibTupling(n-1)
        return (f_n1 + f_n2, f_n1)

#W(n) = S(n) = n
#will cache values between calls, but has O(n) space complexity
def FibMemo(n, memo):
    global calls
    calls += 1

    if (n == 0):
        memo[0] = 0
        return 0
    elif (n == 1):
        memo[1] = 1
        return 1
    else:
        if n in memo:
            return memo[n]
        else:
            n_1 = -1
            if (n-1 in memo):
                n_1 = memo[n-1]
            else:
                n_1 = FibMemo(n-1, memo)
            
            n_2 = -1
            if (n-2 in memo):
                n_2 = memo[n-2]
            else:
                n_2 = FibMemo(n-2, memo)
            
            val = n_1 + n_2
            memo[n] = val
            return val

def main():
    global calls
    n = int(sys.argv[1])

    memo = dict()

    r1 = FibMemo(n, memo)
    print(f"Memoization: {r1}, calls: {calls}")
    calls = 0
    r2, _ = FibTupling(n)
    print(f"Tupling: {r2}, calls: {calls}")
    calls = 0
    r3 = FibStandard(n)
    print(f"Standand (no optimization): {r3}, calls: {calls}")
    calls = 0

    return (r1, r2, r3)

if __name__ == "__main__":
    main()