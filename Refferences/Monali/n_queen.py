"""
n_queen.py
Author: Jagrut Gala
Date: 24-07-2021
Pracitcal: 3
Objective: Demonstarte N-Queen problem and give a solution
"""

def printBoard(board):
    for i in len(board):
        for j in len(i):
            print (j, end = " ")
        print()

def generateBoard(size: int) -> list:
    board= list()
    for i in range(size):
        l= []
        for j in range(size):
            l.append(0)
        board.append(l)
    return(board)

def isQueenSafe():
    pass


print(generateBoard(4))