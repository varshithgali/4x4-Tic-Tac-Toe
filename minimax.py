import copy 
import game_r as game
from math import inf as infinity

max_depth = 9
def winning_possibility(board, player):
    count = 0
    d = 0
    player_cell = []
    
    for x, row in enumerate(board):
        # print(x, row)
        for y, col in enumerate(row):
            if board[x][y] == player:
                player_cell.append([x, y])
    for cell in player_cell:
        if (board[cell[0]][0] == player or board[cell[0]][0] == None) and (board[cell[0]][1] == player or board[cell[0]][1] ==None) and (board[cell[0]][2] == player or board[cell[0]][2] ==None) and (board[cell[0]][3] == player or board[cell[0]][3] ==None):
            count += 1
        if (board[0][cell[1]] == player or board[0][cell[1]] == None) and (board[1][cell[1]] == player or board[1][cell[1]] == None) and (board[2][cell[1]] == player or board[2][cell[1]] == None) and (board[3][cell[1]]== player or board[3][cell[1]]== None):
            count += 1
        if (board[0][0] == player or board[0][0] == None) and (board[1][1] == player or board[1][1] == None) and (board[2][2] == player or board[2][2] == None) and (board[3][3] == player or board[3][3] == None):
            count += 1
        if (board[0][3] == player or board[0][3] == None) and (board[1][2] == player or board[1][2] == None) and (board[2][1] == player or board[2][1] == None ) and (board[3][0] == player or board[3][0] == None):
            count += 1

    return count

def minimax(state, depth, alpha, beta, player):
    wo = winning_possibility(state, "O")
    wx = winning_possibility(state, "X")
    
    if wo == 0 and wx == 0:
        return 0, [4, 4]

    val, winner = game.alignment(state)
    if player == "O":
        nextp = "X"
    else:
        nextp = "O"

    if depth == 0 or val:
        if winner == "O":
            return 10, state
        elif winner == "X":
            return -10, state
        return 0, state

    if game.is_full(state):
        return 0, state

    best_cell = None
    games = game.empty_cells(state)
    for cell in games:
        state[cell[0]][cell[1]] = player
        # G.add_node(str(state))
        val, move = minimax(state, depth-1, alpha, beta, nextp)
        state[cell[0]][cell[1]] = None

        if player == 'O':
            if depth < max_depth:
                best_cell = cell
                val = wo - wx
                return val, best_cell            
            if val > alpha:
                best_cell = cell
                alpha = val
            if alpha >= beta:
                break

        else:
            if depth < max_depth:
                best_cell = cell
                val = wo - wx
                return val, best_cell
            if val < beta:
                best_cell = cell
                beta = val
            if beta <= alpha:
                break

    if player == 'O':
        return alpha, best_cell
    else:
        return beta, best_cell
