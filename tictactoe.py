"""
Tic Tac Toe Player
"""

import math
import copy
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
    NumO = 0
    NumX = 0
    for ele in board:
        NumO += ele.count("O")
        NumX += ele.count("X")
    if NumO == NumX == 0:
        return "X"
    elif NumO >= NumX:
        return "X"
    elif NumO < NumX:
        return "O"
    else:
        return "gameOver"

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionsPossible = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None:
                actionsPossible.add((i,j))
    return actionsPossible


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if (action[0] > 2 or action[0] < 0) or (action[1] > 2 or action[0] < 0):
        raise RuntimeError("invalid move")
    if board[action[0]][action[1]] != None:
        raise RuntimeError("invalid move")
    x = copy.deepcopy(board)
    x[action[0]][action[1]] = player(x)
    return x


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for ele in board:
        if len(set(ele)) == 1:
            if ele[0] != None:
                return ele[0]
    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != None:
            return board[0][i]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    Over = True
    for ele in board:
        for elee in ele:
            if winner(board) != None:
                return True
            elif elee == None:
                Over = False
    return Over



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    actslist = []
    def MaxValue(board):
        if terminal(board):
            return utility(board)
        v = -math.inf
        for act in actions(board):
            actslist.append(act)
            v = max(v,MinValue(result(board,act)))
        return v
    def MinValue(board):
        if terminal(board):
            return utility(board)
        v = math.inf
        for act in actions(board):
            actslist.append(act)
            v = min(v,MaxValue(result(board,act)))
        return v
    if utility(board) == 1:
        return None
    MaxValue(board)
    return actslist[-1]
