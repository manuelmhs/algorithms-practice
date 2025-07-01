"""
Given a positive integer n, find the nth Even Fibonacci number.
1 <= n <= 15
"""

import sys
def main():
    n = int(sys.argv[1])

    f1 = 0
    f2 = 1
    f3 = -1
    odd = True

    while n >= 1:
        f3 = f1 + f2
        if odd:
            f1 = f3
        else:
            f2 = f3

        odd = not odd

        if (f3 % 2) == 0:
             n -= 1

    print(f3)
    return f3

if __name__ == "__main__":
    main()