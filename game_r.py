import numpy as np
import random

import minimax as ai
import gui_r as gui
from math import inf

alpha, beta = -inf, +inf

class Board():
    def __init__(self):
        self.board = np.full((4,4), None)

    def update(self, x, y, symbol):
        if(self.board[x][y] is None):
            self.board[x][y] = symbol
            print(self.board)
            return True
        print("Move not possible")
        return False

    def possible_moves(self, x, y):
        return self.board[x][y] is None

    def __str__(self):
        board_str = ""
        for i, row in enumerate(self.board):
            board_str += "|"
            for j, cell in enumerate(row):
                if(cell is None):
                    board_str += " -"
                else:
                    board_str += " " + self.board[i][j]
            board_str += " |\n"
        return board_str

class Player():
    def __init__(self, name, symbol, AI=False):
        self.name = name
        self.symbol = symbol
        self.AI = AI
        self.won_games = 0
        self.draw_games = 0

    def stat(self):
        return self.name + " won " + str(self.won_games) + " games, " + str(self.draw_games) + " draw."

    def __str__(self):
        return self.name

def alignment(board):
    if(board[0][0] == board[0][1] == board[0][2] == board[0][3] != None):  # horizontal
        return True, board[0][0]
    elif(board[1][0] == board[1][1] == board[1][2] == board[1][3] != None):  # horizontal
        return True, board[1][0]
    elif(board[2][0] == board[2][1] == board[2][2] == board[2][3] != None):  # horizontal
        return True, board[2][0]
    elif(board[3][0] == board[3][1] == board[3][2] == board[3][3] != None):  # horizontal
        return True, board[3][0]
    elif(board[0][0] == board[1][0] == board[2][0] == board[3][0] != None):  # vertical
        return True, board[0][0]
    elif(board[0][1] == board[1][1] == board[2][1] == board[3][1] != None):  # vertical
        return True, board[0][1]
    elif(board[0][2] == board[1][2] == board[2][2] == board[3][2] != None):  # vertical
        return True, board[0][2]
    elif(board[0][3] == board[1][3] == board[2][3] == board[3][3] != None):  #vertical
        return True, board[0][3]
    elif(board[0][0] == board[1][1] == board[2][2] == board[3][3] != None):  # diagonal
        return True, board[0][0]
    elif(board[0][3] == board[1][2] == board[2][1] == board[3][0] != None):  # diagonal
        return True, board[0][3]
    else:
        return False, None


    # if(grid[0][0] == grid[0][1] == grid[0][2] != None):  # horizontal
    #     return True, grid[0][0]
    # elif(grid[1][0] == grid[1][1] == grid[1][2] != None):  # horizontal
    #     return True, grid[1][0]
    # elif(grid[2][0] == grid[2][1] == grid[2][2] != None):  # horizontal
    #     return True, grid[2][0]
    # elif(grid[0][0] == grid[1][0] == grid[2][0] != None):  # vertical
    #     return True, grid[0][0]
    # elif(grid[0][1] == grid[1][1] == grid[2][1] != None):  # vertical
    #     return True, grid[0][1]
    # elif(grid[0][2] == grid[1][2] == grid[2][2] != None):  # vertical
    #     return True, grid[0][2]
    # elif(grid[0][0] == grid[1][1] == grid[2][2] != None):  # diagonal
    #     return True, grid[0][0]
    # elif(grid[1][1] == grid[0][2] == grid[2][0] != None):  # diagonal
    #     return True, grid[1][1]
    # else:
    #     return False, None

def is_full(grid):
    for rows in grid:
        for cell in rows:
            if cell is None:
                return False
    return True


def empty_cells(state):
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell is None:
                cells.append([x, y])
    #print(cells)
    return cells

def game_loop(screen, p1, p2):

    def next_player(turn):
        if(turn == p1):
            return p2
        return p1

    # Initiliaze the Board
    board = Board()

    # Choose random player to start game
    if(random.randint(1, 2) == 1):
        playerTurn = p1
    else:
        playerTurn = p2
    playerTurn = p2

    # Check if player is AI
    if(playerTurn.AI):
        depth = len(empty_cells(board.board))
        if depth == 0:
            return
        if depth == 16:
            x = random.randint(0, 3)
            y = random.randint(0,3)
        else:
            _, move = ai.minimax(board.board, depth,alpha, beta, playerTurn.symbol)
            x, y = move[0], move[1]
            if x == y == 4:
                return 0
        print(f"Cell:{(x, y)}")
        board.update(x, y, playerTurn.symbol)
        gui.drawSymbole(screen, (x, y), playerTurn.symbol)

    else:
        # Get player input
        x, y = gui.playerInput(screen)
        # Check if the cell is not already used
        while not board.possible_moves(x, y):
            x, y = gui.playerInput(screen)
        print(f"Cell:{(x, y)}")
        board.update(x, y, playerTurn.symbol)
        gui.drawSymbole(screen, (x, y), playerTurn.symbol)

    aligned, _ = alignment(board.board)
    while(not aligned and not is_full(board.board)):
        # Switch player
        playerTurn = next_player(playerTurn)

        # Check if player is AI
        if(playerTurn.AI):
            depth = len(empty_cells(board.board))
            if depth == 0:
                return
            if depth == 16:
                x = random.randint(0, 3)
                y = random.randint(0,3)
            else:
                _, move = ai.minimax(board.board, depth, alpha, beta, playerTurn.symbol)
                x, y = move[0], move[1]
                if x == y == 4:
                    return 0
            print(f"Cell:{(x, y)}")
            board.update(x, y, playerTurn.symbol)
            gui.drawSymbole(screen, (x,y), playerTurn.symbol)
        else:
            # Get player input
            x, y = gui.playerInput(screen)
            # Check if the cell is not already used
            while not board.possible_moves(x, y):
                x, y = gui.playerInput(screen)
            print(f"Cell:{(x, y)}")
            board.update(x, y, playerTurn.symbol)
            gui.drawSymbole(screen, (x, y), playerTurn.symbol)

        # Check if there's a winner
        aligned, _ = alignment(board.board)

    if(aligned):
        playerTurn.won_games += 1
        return playerTurn

    elif(is_full(board.board)):
        p1.draw_games += 1
        p2.draw_games += 1
        return 0

if __name__ == "__main__":
    inpt = "y"
    p1 = Player("YOU", "X")
    p2 = Player("AI", "O", AI=True)
    screen = gui.init()

    while(inpt != "n"):

        # Start the game loop
        winner = game_loop(screen, p1, p2)

        if(winner != 0):
            gui.writeScreen(screen, winner.name + " won!")
        else:
            gui.writeScreen(screen, "Draw!", line=1)

        gui.writeScreen(screen, "Click to", line=2)
        gui.ask(screen, " play again!", line=3)
        gui.clearScreen(screen)
        print(p1.stat())
        print(p2.stat())
