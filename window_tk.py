import tkinter as tk
# from board import TicTacToeBoard
import board

class TicTacToeApp(tk.Tk):
    def __init__(self, board):
        super().__init__()
        self._board = board
        self.init_state()
        self.init_components()
        self.update()


    def init_state(self):
        """Initalises game status attributes"""

        self._current_marker = 'X'   # Current player. X starts
        self._is_running = True      # Is game running? It's set to False
                                     # when someone wins or board is full.


    def init_components(self):
        """Create graphical components and place them in a grid layout"""

        self.title('Tre-i-rad')     # Window title
        self.geometry('300x330')    # Window size

        # Create 3x3 buttons and store them in a matrix (self._buttons)
        self._buttons = []
        for row in range(3):
            t = []
            for col in range(3):
                button = tk.Button(self,
                    font=('Helvetica', 40),
                    anchor='center',
                    width=1,
                    background="white",
                    # Make each button call method "clicked" when they are
                    # clicked on, with the right argument values (row and col).
                    command=lambda r=row,c=col: self.clicked(r, c))
                # Place buttons in grid layout
                button.grid(row=row, column=col, sticky="NEWS")
                t.append(button)
            self._buttons.append(t)

        # Create label for the status of the game in the bottom left
        self._label = tk.Label(self,
                        font=('Helvetica', 30),
                        anchor='center',
                        width=2)
        self._label.grid(row=3, column=0, columnspan=2, sticky="NEWS")

        # Create restart button in the bottom right
        self._restart_button = tk.Button(self,
                    text='Restart!',
                    width=1,
                    # Connect button to method restart_clicked()
                    command=self.restart_clicked)
        self._restart_button.grid(row=3, column=2, sticky="NEWS")

        # Expand components to window size and handle window resize
        for i in range(3):
            self.columnconfigure(i, weight=3)
            self.rowconfigure(i, weight=3)
        self.rowconfigure(3, weight=1)


    def clicked(self, row, col):
        """This method is called when the user clicks on any of the 3x3 buttons"""

        # Only place marker if the game is running and the place is empty
        if self._is_running and board.is_empty(self._board,row, col):
            # Place marker at row/col
            board.place(self._board, self._current_marker, row, col)
            # Change current player (marker) to the next player
            if self._current_marker == 'X':
                self._current_marker = 'O'
            else:
                self._current_marker = 'X'

            # Update graphical components etc
            self.update()


    def restart_clicked(self):
        """This method is called when the user clicks on the restart button"""

        self.init_state()
        self._board = board.new_board()
        self.update()


    def update(self):
        """Updates all graphical components according to the state of the board"""

        # Update all buttons according to the current state of the board
        for row in range(3):
            for col in range(3):
                button = self._buttons[row][col]   # Get (graphical) button
                marker = board.get(self._board, row, col) # Get value from board
                # Update text for button to either 'X', 'O' or ''
                if marker != '-':
                    button['text'] = marker
                else:
                    button['text'] = ''

        # Update status label and if game is still running
        if board.is_winner(self._board, 'X'):
            self._label['text'] = 'X wins!'
            self._is_running = False
        elif board.is_winner(self._board, 'O'):
            self._label['text'] = 'O wins!'
            self._is_running = False
        elif board.is_full(self._board):
            self._label['text'] = 'Ex aequo!'
            self._is_running = False
        else:
            self._label['text'] = f'{self._current_marker}:s tur'


if __name__ == '__main__':
    board_ = board.new_board()
    app = TicTacToeApp(board_)
    app.mainloop()