import random

# 2-3 survives
#100
#011
#000
# 4+ dies
#100      100
#111 -->  101
#100      100
# 1- dies
#000      000
#011  --> 001 
#000      000
# birth 3
#100       100
#001  -->  011
#100       100

def generate_matrix(board):
    for y in range(len(board))
        for x in range(len())


def generate_random_lifes(board, lifes):
        new_board = board
        life_list = []
        while len(life_list) < lifes:
            y = random.randint(0, len(board[0])-1)
            x = random.randint(0, len(board)-1)
            coords = (x, y)
            if coords not in life_list:
                life_list.append(coords)
        for coord in life_list:
            x, y = coord
            new_board[x][y] = "[0]"
        
        return new_board

