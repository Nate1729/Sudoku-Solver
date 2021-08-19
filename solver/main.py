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
