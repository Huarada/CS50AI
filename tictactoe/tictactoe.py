"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None
BOARD_SIZE = 3 # bcz the tictactoe board is 3X3


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
    counter_O = sum(row.count(O) for row in board)
    counter_X = sum(row.count(X) for row in board)
    
    return O if counter_O != counter_X else X
    
    
    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    final = set()
    
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == EMPTY:
                final.add((i,j))
    return final
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #raise NotImplementedError
    if action not in actions(board):
        raise Exception("Error with the action")
    
    board_copia = copy.deepcopy(board)
    
    row,col = action
    board_copia[row][col] = player(board)
    return board_copia
    

def checkRow(board, player):
    for row in range(len(board)):
        if (board[row][0] == player) and (board[row][1] == player) and (board[row][2] == player):
            return True
    return False

def checkcol(board,player):
    for col in range(BOARD_SIZE):
        if (board[0][col]== player) and (board[1][col] == player) and (board[2][col] == player) :
            return True
    return False

def checkdig(board, player):
    count = 0
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if row == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True #there is a winner, 3 reps in a col or row
    else:
        return False

def checkdigTwo(board, player):
    count = 0
    for row in range(BOARD_SIZE):
        for col in range(len(board[row])):
            if (len(board) - row - 1) == col and board[row][col] == player:
                count += 1
    
    if count == 3:
        return True
    else:
        return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #raise NotImplementedError
    if checkRow(board , X) or checkcol(board, X) or checkdig(board, X) or checkdigTwo(board, X):
        return X
    elif checkRow(board , O) or checkcol(board, O) or checkdig(board, O) or checkdigTwo(board, O):
        return O
    
    else: return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #raise NotImplementedError
    if winner(board) == X:
        return True
    if winner(board) == O:
        return True
    
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #raise NotImplementedError
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    
    return v    


def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    
    return v
    


    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #raise NotImplementedError
    if terminal(board) :
        return None
    
    elif (player(board)) == X:
        plays =[]
        
        for action in actions(board):
            plays.append([min_value(result(board, action)),action])
            
        return sorted(plays, key = lambda x: x[0], reverse = True)[0][1]
    
    elif (player(board)) == O:
        plays =[]
        
        for action in actions(board):
            plays.append([max_value(result(board, action)),action])
            
        return sorted(plays, key = lambda x: x[0])[0][1]    