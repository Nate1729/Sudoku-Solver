""" This script solves a sudoku board using backtracking
"""
arr_board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
             [6, 0, 0, 1, 9, 5, 0, 0, 0],
             [0, 9, 8, 0, 0, 0, 0, 6, 0],
             [8, 0, 0, 0, 6, 0, 0, 0, 3],
             [4, 0, 0, 8, 0, 3, 0, 0, 1],
             [7, 0, 0, 0, 2, 0, 0, 0, 6],
             [0, 6, 0, 0, 0, 0, 2, 8, 0],
             [0, 0, 0, 4, 1, 9, 0, 0, 5],
             [0, 0, 0, 0, 8, 0, 0, 7, 9]]

def test_row(arr_board, row, test_num):
    """ This test if an input is valid.
    True  ==> input is valid
    False ==> input is not valid"""
    
    for i in range(9):
        if arr_board[row][i] == test_num:
            return False
    return True


def test_col(arr_board, col, test_num):
    """ This tests if a n input is valid 
    in its column.
    True  ==> input is valid
    False ==> input is not valid."""

    for i in range(9):
        if arr_board[i][col] == test_num:
            return False
    return True

def test_square(arr_board, square_row, square_col, test_num):
    """ This tests if an input is valid based on 
    the local 3x3 grid. The numbering system for the grid 
    goes like this (it makes the math easier).
    +-------+-------+-------+
    | (0,0) | (0,1) | (0,2) |
    +-------+-------+-------+
    | (1,0) | (1,1) | (1,2) |
    +-------+-------+-------+
    | (2,0) | (2,1) | (2,2) |
    +-------+-------+-------+
    True  --> input is valid
    False --> input is NOT valid
    """
    for r in [3*square_row + i for i in range(3)]:
        for c in [3*square_col + i for i in range(3)]:
            if arr_board[r][c] == test_num:
                return False
    return True

def test_input(arr_board, row, col, test_num):
    """ This test is an input is valid by checking
    row, col, and sub_square.
    True  --> input is valid
    False --> input is not valid
    """
    
    # Convert/find square indecies
    square_row = row // 3
    square_col = col // 3

    if test_row(arr_board, row, test_num) and test_col(arr_board, col, test_num) and test_square(arr_board, square_row, square_col, test_num):
        return True
    else:
        return False

def solve_board(arr_board, row, col):
    """This fills in entries in the ind_fill recursively
    to fill out the sudoku board"""

    # === Base Cases === #
    # Case 1: End of the grid
    if row == 8 and col == 9:
        # We are done
        # Let's Print the result
        for row in range(9):
            print(arr_board[row])
        return True
    
    # Case 2: End of a row
    if col == 9:
        row += 1
        col = 0
    
    # Case 3: There is already a number there
    if arr_board[row][col] > 0:
        return solve_board(arr_board, row, col+1)
    # Recursively iterate through possible value

    for val in range(1,10):
        # Check if placement is valid
        if test_input(arr_board, row, col, val):
            # The number works
            # We add the number in
            arr_board[row][col] = val

            # Now we move onto the next entry
            if solve_board(arr_board, row, col + 1):
                # This makes the recursion work
                return True
                
        # If this num didn't pan out we should reset it
        arr_board[row][col] = 0
    return False

if (solve_board(arr_board, 0, 0)):
    print('It worked')
else:
    print('It failed')

        

