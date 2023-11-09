"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    moves = 0

    for row in board:
        for col in row:
            if col != None:
                moves += 1

    if moves % 2 == 0:
        return X
    else:
        return O
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions = set()

    for id1, row in board:
        for id2, col in row:
            if col != X and col != O and col != EMPTY:
                actions.add((id1, id2))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = board
    new_board[action[0]][action[1]] = player(board)

    return new_board
    # Todo raise exception on bad board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for row in board:
        last_action = 'no_action'
        win_counter = 0
        for col in row:
            if last_action == col and col != None:
                win_counter += 1
            
            if win_counter == 2:
                return col
            
            last_action = col
    
    for i in range(3):
        last_action = 'no_action'
        win_counter = 0
        for j in range(3):
            if last_action == board[j][i] and board[j][i] != None:
                win_counter += 1
            
            if win_counter == 2:
                return board[j][i]
            
            last_action = board[j][i]
    
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != None:
        return board[1][1]
    
    if board[2][0] == board[1][1] == board[0][2] and board[1][1] != None:
        return board[1][1]
    
    return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    check_win = winner(board)
    if check_win == X or check_win == O or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    check_win = winner(board)
    if check_win == X:
        return 1
    elif check_win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError