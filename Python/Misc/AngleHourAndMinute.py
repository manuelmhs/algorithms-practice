"""
Given the time represented by two integers h (hour) and m (minute), calculate the angle between the hour hand and the minute hand
on a standard 12-hour clock.

Note: There can be two angles between hands; we need to print a minimum of two. Also, we need to print the floor of the final result angle.
For example, if the final angle is 10.61, we need to print 10.

1 ≤ h ≤ 12
0 ≤ m < 60
"""

import sys
from math import floor

def main():
    h = float(sys.argv[1])
    m = float(sys.argv[2])

    degreeH = ((360 / 12) * h) + ((((360 / 60) / 12) * m)) % 360
    degreeM = ((360 / 60) * m) % 360

    degreeHM = floor(degreeH - degreeM)

    if degreeHM > 180:
        degreeHM -= 180

    degreeHM = abs(degreeHM)

    print(degreeHM)
    return degreeHM



if __name__ == "__main__":
    main()