"""
File Name: board.py
Author: Samuel Jeffman
Date: 2024-11-24
Description: Programming in Python: Basic and Preparatory Course, Assignment 4. Tic-tac-toe app.
"""

# Create new board, 3x3 empty('-') cells
def new_board():
    board = []
    for row in range(3):
        new_row = []
        for col in range(3):
            new_row.append('-')
        board.append(new_row)
    return board

# Assert for new_board()
assert new_board() ==   [['-','-','-'],
                         ['-','-','-'],
                         ['-','-','-']]

# Return a specific position in the matrix
def get(board, row, col):
    return board[row][col]

# Assert for get()
assert get(new_board(), 0, 0) == '-'
assert get(new_board(), 2, 2) == '-'

# Returns True if cell is empty('-')
def is_empty(board, row, col):
    return board[row][col] == '-'

# Assert for is_empty()
assert is_empty(new_board(), 0,0) == True
assert is_empty(new_board(), 2,2) == True

# Returns the width of the board
def get_width(board):
    return len(board[0])

# Returns the height of the board
def get_height(board):
    return len(board)

# Asserts for width and height
assert get_width(new_board()) == 3
assert get_height(new_board()) == 3

# Prints the board to screen
def print_board(board):
    for row in range(get_height(board)):
        for col in range(get_width(board)):
            print(board[row][col], end=' ')
        print('')
    print('\n')
    return 0
###
# Don't really know how to assert things that are printed to screen
###

# Place a marker at a specific position if it is empty, otherwise return False
def place(board, marker, row, col) -> None:
    if is_empty(board, row, col):
        board[row][col] = marker
        return True
    return False

# Assert for place()
assert place(new_board(), 'X', 0,0) == True
assert place(new_board(), 'O', 1,1) == True
board0 = new_board()
place(board0,'X', 0, 0)
place(board0,'X', 1, 0)
place(board0,'X', 2, 0)
place(board0,'X', 0, 1)
place(board0,'X', 1, 1)
place(board0,'X', 2, 1)
place(board0,'X', 0, 2)
place(board0,'X', 1, 2)
place(board0,'X', 2, 2)
assert place(board0, 'X', 0,0) == False
assert place(board0, 'O', 1,1) == False

# Returns True if there are no empty cells left
def is_full(board):
    for row in range(get_height(board)):
        for col in range(get_width(board)):
            if board[row][col] == '-':
                return False
    return True

# Assert for is_full()
assert is_full(new_board()) == False
board0 = new_board()
place(board0,'X', 0, 0)
place(board0,'X', 1, 0)
place(board0,'X', 2, 0)
place(board0,'X', 0, 1)
place(board0,'X', 1, 1)
place(board0,'X', 2, 1)
place(board0,'X', 0, 2)
place(board0,'X', 1, 2)
place(board0,'X', 2, 2)
assert is_full(board0) == True

# Check if specific "marker" is winner or not.
# Checks for 3 in a row, column or diagonal
def is_winner(board, marker):
    height = get_height(board)
    width = get_width(board)
    length = 3

    # Check rows/cols
    for row in range(height):
        row_count = 0
        col_count = 0
        for col in range(width):
            # Check row
            if board[row][col] == marker:
                row_count += 1
                if row_count >= length:
                    return True
            else:
                row_count = 0

            # Check column
            if board[col][row] == marker:
                col_count += 1
                if col_count >= length:
                    return True
            else:
                col_count = 0
    # Check diagonally
    if height/width == 1: # Only possible if matrix is square
        diag_count1 = 0
        diag_count2 = 0
        for row in range(height):
            # Check diagonally \
            col = row
            if board[row][col] == marker:
                diag_count1 += 1
                if diag_count1 >= length:
                    return True
            else:
                diag_count1 = 0

            # Check diagonally /
            col = height - 1 - row # -1 because arrays are 0-based
            if board[row][col] == marker:
                diag_count2 += 1
                if diag_count2 >= length:
                    return True
            else:
                diag_count2 = 0
    return False

# Assert for is_winner()
board1 = new_board()
place(board1,'X', 0, 1)
place(board1,'X', 1, 1)
place(board1,'X', 2, 1)
assert is_winner(new_board(), 'X') == False
assert is_winner(board1, 'X') == True
assert is_winner(board1, 'O') == False

if __name__ == '__main__':
    #... Test code for the functions, for example ...
    board2 = new_board()
    place(board2, 'X', 0, 0)
    print_board(board2)
    place(board2, 'O', 0, 0)
    place(board2, 'O', 1, 0)
    print_board(board2)
    place(board2, 'X', 1, 1)
    print_board(board2)
    place(board2, 'O', 2, 2)
    print_board(board2)
    place(board2, 'X', 0, 1)
    print_board(board2)
    place(board2, 'O', 1, 2)
    print_board(board2)
    place(board2, 'X', 2, 1)
    print_board(board2)
    print("O wins?","Yes" if is_winner(board2, 'O') else "No")
    print("X wins?","Yes" if is_winner(board2, 'X') else "No")