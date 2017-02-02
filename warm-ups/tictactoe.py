"""
If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved.

Write a function that takes a list of lists and returns a boolean game if the game has a winner.

Assume that the board comes in the form of a 3x3 list of lists, where the vaule is 0 if the spot is empty, 1 if it is an X, or 2 if an O.



>>> tic_tac_toe([1,0,0],[1,0,0][1,0,0])
Winner!

>>> tic_tac_toe([2,0,0],[2,0,0][2,0,0])
Winner!

>>> tic_tac_toe([1,0,0],[0,1,0][0,0,1])
Winner!

>>> tic_tac_toe([2,0,0],[0,2,0][0,0,2])
Winner!

>>> tic_tac_toe([0,0,0],[0,0,0],[0,0,0])
No winner.

"""


def diag_check(board):
    if bool(board[0][0] == board[1][1] == board[2][2]):
        return True
    elif bool(board[2][0] == board[1][1] == board[0][2]):
        return True
    else:
        return False


def tic_tac_toe(board):
    cols = list(zip(*board))
    for row, col in zip(board, cols):
        if (sum(row) == 3 and (0 not in row)) or (sum(row) == 6):
            return True
        if (sum(col) == 3 and (0 not in col)) or (sum(col) == 6):
            return True
        if diag_check == True:
            return True
        else:
            return False
    if True:
        print('Winner!')
    if False:
        print('No winner.')