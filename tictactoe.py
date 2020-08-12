"""
Tic Tac Toe Player
"""

import math,copy
value=0
X = "X"
O = "O"
EMPTY = None
board_vals=[]
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
    global O,X,EMPTY
    count=0
    for i in range(len(board)):
        for j in range(len(board[i])):
           if board[i][j]!=EMPTY:
               count +=1
    if count %2==1:
        return O
    else:
        return X
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    global O,X,EMPTY
    answer=[]
    answer=set(answer)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==EMPTY:
                answer.add((i,j))
    return answer
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    global O,X,EMPTY
    board1 = copy.deepcopy(board)
    turn = player(board)
    try:
        if board1[action[0]][action[1]] ==EMPTY:
            board1[action[0]][action[1]] = turn
        else:
            raise Exception("Error")
    except:
        raise Exception("Error")
    return board1
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    global X,O,EMPTY
    i=0
    j=0
    if board[i][j]!=EMPTY:
        if board[i][j] == board[i][j+1] and board[i][j]==board[i][j+2]:
            return board[i][j]
        elif board[i][j] == board[i+1][j] and board[i+2][j]==board[i][j]:
            return board[i][j]
        elif board[i][j]==board[i+1][j+1] and board[i+2][j+2]==board[i][j]:
            return board[i][j]
    j=2
    if board[i][j]!=EMPTY:
        if board[i][j]==board[i+1][j] and board[i+2][j]==board[i][j]:
            return board[i][j]
        elif board[i][j] == board[i+1][j-1] and board[i][j]==board[i+2][j-2]:
            return board[i][j]
    i=2
    if board[i][j]!=EMPTY:
        if board[i][j] == board[i][j-1] and board[i][j-2]==board[i][j]:
            return board[i][j]
    j=1
    i=1
    if board[i][j]!=EMPTY:
        if board[i][j]==board[i-1][j] and board[i+1][j]==board[i][j]:
            return board[i][j]
        elif board[i][j] == board[i][j-1] and board[i][j]==board[i][j+1]:
            return board[i][j]
    return None
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    counter=0
    if not winner(board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] ==EMPTY:
                    counter +=1
                    break
    if counter==0:
        return True
    else:
        return False
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    global O,X,EMPTY
    temp=winner(board)
    if temp:
        if temp==O:
            return -1
        else:
            return 1
    else:
        return 0
def minimax(board,value=0):
    """
    Returns the optimal action for the current player on the board.
    """
    play = player(board)
    if terminal(board)==True:
        return None
    else:
        actions_avail = actions(board)
        if play==X:
            maxi = -1000
            for action in actions_avail:
                board2 = result(board,action)
                temp = minimax(board2)
                if not temp:
                    temp1 = utility(board2)
                    if temp1>=maxi:
                        maxi= temp1+0
                        answer = copy.deepcopy(action)
                        print(answer,":",value)
                        value=temp1
                else:
                    temp1=temp[1]
                    temp2=temp[0]
                    if temp1>=maxi:
                        answer=copy.deepcopy(action)
                        maxi = temp1+0
                        value=temp1+0
        else:
            mini = 1000
            for action in actions_avail:
                board2 = result(board,action)
                temp= minimax(board2)
                if not temp:
                    temp1 = utility(board2)
                    if temp1<=mini:
                        mini = temp1+0
                        answer = copy.deepcopy(action)
                        print(answer,value)
                        value=temp1
                else:
                    temp1=temp[1]
                    temp2=temp[0]
                    if temp1<=mini:
                        answer= copy.deepcopy(action)
                        mini= temp1+0
                        value=temp1+0
        return [answer,value]
