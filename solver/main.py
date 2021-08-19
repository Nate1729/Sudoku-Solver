""" This script solves a sudoku board using backtracking
"""

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

    if test_row(arr_board, row, test_num)
        and test_col(arr_board, col, test_num)
        and test_square(arr_board, square_row, square_col, test_num):
        return True
    else:
        return False
