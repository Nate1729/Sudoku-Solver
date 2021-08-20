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

def find_empty_cells(arr_board):
    """ This returns a list of tuples 
    off all of the locations which contain 
    a 0 in the sudoku board"""
    ind_empty=  []
    for row in range(9):
        for col in range(9):
            if arr_board[row][col] == 0:
                ind_empty.append((row, col))

    return ind_empty

print(find_empty_cells(arr_board))
