# FILL THIS FILE

# Create new board, 3x3 empty('-') cells
def new_board():
    board = []
    for r in range(3):
        new_row = []
        for c in range(3):
            new_row.append('-')
        board.append(new_row)
    return board

# Return a specific position in the matrix
def get(board, row, col):
    return board[row][col]

# Returns True if cell is empty('-')
def is_empty(board, row, col):
    return board[row][col] == '-'

# Returns the width of the board
def get_width(board):
    return len(board[0])

# Returns the height of the board
def get_height(board):
    return len(board)

# Prints the board to screen
def print_board(board):
    for row in range(get_height(board)):
        for col in range(get_width(board)):
            print(board[row][col], end=' ')
        print('')
    return 0

# Place a marker at a specific position if it is empty, otherwise return False
def place(board, marker, row, col):
    if is_empty(board, row, col):
        board[row][col] = marker
        return True
    return False

# Returns True if there are no empty cells left
def is_full(board):
    for row in range(get_height(board)):
        for col in range(get_width(board)):
            if board[row][col] == '-':
                return False
    return True

# Check if specific "marker" is winner or not.
# Checks for 3 in a row, column or diagonal
def is_winner(board, marker):
    height = get_height(board)
    width = get_width(board)
    length = 3

    # Check ros/cols
    row_count = 0
    col_count = 0
    for row in range(height):
        for col in range(width):
            # Check rows
            if board[row][col] == marker:
                row_count += 1
                if row_count >= length:
                    return True
            else:
                row_count = 0

            # Check columns
            if board[col][row] == marker:
                col_count += 1
                if col_count >= length:
                    return True
            else:
                col_count = 0
    # Check diagonal
    diag_count1 = 0
    diag_count2 = 0
    if height/width == 1: # Only possible if matrix is square
        for row in range(height):

            # Search diagonally \
            col = row
            if board[row][col] == marker:
                diag_count1 += 1
                if diag_count1 >= length:
                    return True
            else:
                diag_count1 = 0
            
            # Search diagonally /
            col = height - row - 1
            if board[row][col] == marker:
                diag_count2 += 1
                if diag_count2 >= length:
                    return True
            else:
                diag_count2 = 0
    return False