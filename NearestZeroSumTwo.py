"""
Given a list of Int (positive or negative), find the (x,y) pair of numbers which sum (x+y) is nearest to 0.
Assume there's at least 2 numbers in the list.
"""

import sys

def aux(t1,t2):
    a,b = t1
    x,y = t2
    if abs(a+b) <= abs(x+y):
        return t1
    else:
        return t2

def main():
    list = []
    for n in sys.argv[1:]:
        list.append(int(n))

    a = list[0]
    b = list[1]

    for i, n in enumerate(list[:len(list)-1]):
        a,b = aux((a,b), (n,list[i+1]))

        if a+b == 0:
            break
        
        for m in list[i+2:]:
            a,b = aux((a,b), (n,m))

    print(f"({a},{b})")
    return (a,b)

if __name__ == "__main__":
    main()