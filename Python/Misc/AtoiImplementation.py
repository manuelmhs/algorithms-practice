"""
Given a string s, the objective is to convert it into integer format without utilizing any built-in functions.
Refer the below steps to know about atoi() function.

Cases for atoi() conversion:
    Skip any leading whitespaces.
    Check for a sign (+ or -), default to positive if no sign is present.
    Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached.
        If no digits are present, return 0.
    If the integer is greater than (2^31)-1, then return (2^31)-1 and if the integer is smaller than -(2^31), then return -(2^31).
"""

import sys

def Atoi(str):
    l = len(str)
    idx = 0

    # skip leading chars
    while (idx < l and not str[idx].isdigit()):
        idx += 1

    if idx == l: # there's no numbers
        return 0
    else:
        lower = -(2**31)
        upper = (2**31)-1
        
        factor = 1
        if (idx > 0 and str[idx-1] == "-"): # short circuited and
            factor = -1
        
        # read the digits, leading zeros won't change the result
        n = 0
        while (idx < l and str[idx].isdigit() and n <= upper+1):
            n *= 10
            n += int(str[idx])
            idx += 1

        n *= factor

        n = min(n, upper)
        n = max(n, lower)

        return n

def main():
    str = sys.argv[1]

    n = Atoi(str)

    print(n)
    return n

if __name__ == "__main__":
    main()