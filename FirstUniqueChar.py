"""
Given a lower-case string, find the first unique character in it.
If all characters are repeated, return None.
"""

import sys
from collections import deque #OrderedDict or other structure that supports O(1) search would be better

def main():
    string = sys.argv[1]

    order = deque()
    forbidden = [] #same, search isn't efficient

    for c in string:
        if c in forbidden:
            continue
        if c in order:
            order.remove(c)
            forbidden.append(c)
        else:
            order.append(c)

    res = None
    if order:
        res = order.popleft()

    print(res)
    return res

if __name__ == "__main__":
    main()