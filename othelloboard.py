import random
import sys

def drawBoard(board):

    horizontal = '-|-|-|-|-|'
    vertical = '||||||||'

    print(' 1 2 3 4 5 6 7 8')

    print(horizontal)
    for y in range (8):
        print(vertical)
        print(y+1, end='')
        for x in range(8):
            print('|%s(board[x][y]),end=')
            print("|")
            print(vertical)
            print(horizontal)


def getNewBoard():
    board = []
    for i in range(8):
        board.append(['']*8)
        return board

def resetBoard(board):
    for x in range (8):
        for y in range (8):
            board[x][y]=''

    board[3][3]='X'
    board[3][4]='X'
    board[4][3]='X'
    board[4][4]='X'


def main():
    mainBoard = getNewBoard()
    resetBoard(mainBoard)


def print_horiz_line():
    print("---" * board_size)

def print_vert_line():
    print("|  "*(board_size + 1))

print('Welcome to Othello!')
board_size = int(input("How many rows do you want your board to be?"))
print('Hint: Othello has 64 squares, so you would enter 8')

for index in range(board_size):
    print_horiz_line()
    print_vert_line()


