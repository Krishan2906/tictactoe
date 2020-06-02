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
    cntX=0
    cntO=0
    for i in range(3):
        for j in range(3):
            if board[i][j]=="X":
                cntX+=1
            elif board[i][j]=="O":
                cntO+=1
    if cntX==cntO:
        return X
    elif cntX==cntO+1:
        return O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action=set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                action.add((i,j))
    if len(action)!=0:
        return action
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    import copy
    turn=player(board)
    brd=copy.deepcopy(board)
    brd[action[0]][action[1]]=turn
    return brd
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0]==board[0][1] and board[0][1]==board[0][2]:
        return board[0][0]
    elif board[0][0]==board[1][0] and board[1][0]==board[2][0]:
        return board[0][0]
    elif board[0][0]==board[1][1] and board[1][1]==board[2][2]:
        return board[0][0]
    if board[2][2]==board[2][1] and board[2][1]==board[2][0]:
        return board[2][0]
    elif board[2][2]==board[1][2] and board[1][2]==board[0][2]:
        return board[0][2]
    elif board[0][2]==board[1][1] and board[1][1]==board[2][0]:
        return board[2][0]
    elif board[1][0]==board[1][1] and board[1][1]==board[1][2]:
        return board[1][0]
    elif board[0][1]==board[1][1] and board[1][1]==board[2][1]:
        return board[0][1]
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                return False
    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    champ=winner(board)
    if champ is X:
        return 1
    elif champ is O:
        return -1
    elif champ is None:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal(board)):
        return None
    turn=player(board)
    if turn==X:
        v=float('-inf')
        action=actions(board)
        mv=(-1,-1)
        for (i,j) in action:
            val=minval(result(board,(i,j)))
            if val>=v:
                v=val
                mv=(i,j)
    else:
        v=float('inf')
        action=actions(board)
        mv=(-1,-1)
        for (i,j) in action:
            val=maxval(result(board,(i,j)))
            if val<=v:
                v=val
                mv=(i,j)
    return mv
    raise NotImplementedError


def maxval(board):
    if terminal(board):
        return utility(board)
    action=actions(board)
    v=float('-inf')
    for (i,j) in action:
        v=max(v,minval(result(board,(i,j))))
    return v
    raise NotImplementedError


def minval(board):
    if terminal(board):
        return utility(board)
    action=actions(board)
    v=float('inf')
    for (i,j) in action:
        v=min(v,maxval(result(board,(i,j))))
    return v
    raise NotImplementedError
