"""
Given an integer n, the task is to find the solution to the n-queens problem,
where n queens are placed on an n*n chessboard such that no two queens can attack each other.

The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.
"""

import sys

def isValidPos(column : int, row : int, columns : set, diags1 : set, diags2 : set) -> bool:

    """ this a not so efficient way to check for collisions, iterating through all the already positioned queens
    for i in range(n-remaining):
        otherColumn = l[i][0]
        otherRow = l[i][1]
        if (column == otherColumn or row == otherRow or
            (column + row) == (otherColumn + otherRow) or
            (column - row) == (otherColumn - otherRow)):
            ret = False
            break
    
    return ret
    """

    #instead, we save each column and diagonal already occupied in a set and check if the new position is taken
    diag1 = column + row
    diag2 = column - row
    return not (column in columns or diag1 in diags1 or diag2 in diags2)

def recursive(n : int, remaining : int, l : list, columns : set = set(), diags1 : set = set(), diags2 : set = set()):
    #the recursion is used (implicitly) to advance rows, so in each call we just need to check the columns
    row = n - remaining
    column = 0
    ret = False
    #last queen, we check for each possible column and return
    if (remaining) == 1:
        while (column < n and not ret):
            if isValidPos(column, row, columns, diags1, diags2):
                #columns.add(column) unnecessary because it's the last queen
                #diags1.add(column + row)
                #diags2.add(column - row)
                l[row] = (column, row)
                ret = True
            else:
                column += 1
            
        return ret
    #recursive case, we insert the queen in the first available column and use recursion
    #if there's no recursive solution, we have to advance a column
    #if there's no more columns to advance, there's no global solution
    else:
        while (column < n and not ret):
            if isValidPos(column, row, columns, diags1, diags2):
                columns.add(column)
                diags1.add(column + row)
                diags2.add(column - row)
                l[row] = (column, row)

                ret = recursive(n, remaining-1, l)

                if not ret:
                    columns.remove(column)
                    diags1.remove(column + row)
                    diags2.remove(column - row)

            if not ret:
                column += 1
        
        return ret         

def NQueens(n):
    l = [None] * n
    return (recursive(n, n, l), l)

def main():
    n = int(sys.argv[1])

    r = NQueens(n)

    print(r)
    return r

if __name__ == "__main__":
    main()