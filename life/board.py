import sys
from functions import *

class board():    

    
    def __init__(self, rows, colls, lifes):
        if rows*colls < lifes:
            print("too much lifes")
            sys.exit()
        self.lifes = lifes
        self.board = []
        for i in range(rows):
            self.board.append([])
            for k in range(colls):
                self.board[i].append("[ ]")
        self.board = generate_random_lifes(self.board, lifes)

    def print_board(self):
        print("\n\n\n")
        for i in range(len(self.board)):
            row = ""
            for k in range(len(self.board[i])):
                row += self.board[i][k]
            print(row)
        

    def update(self):

            
