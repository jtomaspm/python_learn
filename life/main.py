import time
from board import *

def main():
    for i in range(1000):
        b = board(20, 20, 20)
        b.print_board()
        time .sleep(.3)



main()