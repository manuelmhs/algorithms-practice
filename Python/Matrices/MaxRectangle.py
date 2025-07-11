"""
Given a binary matrix mat[][] of size n * m. Find the maximum area of a rectangle formed only of 1s in the given matrix.

Input: mat[][] = [[0, 1, 1, 0],
                  [1, 1, 1, 1],
                  [1, 1, 1, 1],
                  [1, 1, 0, 0]]
Output: 8

Input: mat[][] = [[0, 1, 1],
                  [1, 1, 1],
                  [0, 1, 1]]
Output: 6
"""

import sys

def FullRect(mat, ULVertex, DRVertex):
    # checks if the sub-matrix between (up, left) and (down, right) is only composed of 1
    # iterating through all it's elements
    up, left = ULVertex
    down, right = DRVertex

    full = True
    for i in range(up, down+1):
        for j in range(left, right+1):
            if mat[i][j] != 1:
                full = False

    return full

# the idea is: we go through the entire matrix from left-up to right-down, calculating in each step
# the maximum rectangle that contains the actual element as it's top-left vertex
# with recursion we retrieve the max value between this one, and the max from the rest of the elements
def MaxRectangle(mat : list[list[int]], i=-1, j=-1, area=-1, vertex=(-1, -1)):
    # default params, could be also implemented by an aux function
    if i == j == area == -1:
        i = j = area = 0
    
    rows = len(mat)
    columns = len(mat[0])

    # base case, we add the element to the actual area
    if i == rows-1 and j == columns-1:
        return area + mat[i][j]
    else:
        # boundaries of the matrix
        downLimit = i >= rows-1
        rightLimit = j >= columns-1

        # if we land on a 0, we just return the best recursive area
        # (because this element can't be part of a full rectangle)
        if mat[i][j] == 0:
            recArea = 0
            if not rightLimit:
                recArea = MaxRectangle(mat, i, j+1, 0, (-1, -1))
            elif not downLimit:
                recArea = MaxRectangle(mat, i+1, 0, 0, (-1, -1))
            
            return recArea

        # we mark this element as left-upper vertex if we just started calculating a new area
        if area == 0:
            vertex = (i, j)

        # this is the area of the current call
        actualArea = area + mat[i][j]

        # we recursively go to the right, down, and diagonal path in each step if possible
        # and retrieve each recursive area
        area1 = area2 = area3 = -1
        if not rightLimit:
            if FullRect(mat, vertex, (i, j+1)):
                area1 = MaxRectangle(mat, i, j+1, area+1, vertex)

        if not downLimit:
            if FullRect(mat, vertex, (i+1, j)):
                area2 = MaxRectangle(mat, i+1, j, area+1, vertex)

        if not rightLimit and not downLimit:
            if FullRect(mat, vertex, (i+1, j+1)):
                k = (i+1 - vertex[0]) + (j+1 - vertex[1]) + 1
                area3 = MaxRectangle(mat, i+1, j+1, area+k, vertex)

        # we calculate recursively the best area of the rest of the matrix leaving out this element
        recArea = 0
        if not rightLimit:
            recArea = MaxRectangle(mat, i, j+1, 0, (-1, -1))
        elif not downLimit:
            recArea = MaxRectangle(mat, i+1, 0, 0, (-1, -1))

        # finally, the best area is between all this possible ones
        return max(area1, area2, area3, actualArea, recArea)

def main():
    mat = []
    row = []
    for k in sys.argv[1:]:
        if k == "b":
            mat += [row]
            row = []
        else:
            row.append(int(k))

    if row != []:
        mat += [row]

    n = MaxRectangle(mat)

    print(n)
    return n

if __name__ == "__main__":
    main()