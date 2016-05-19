import random

def showGrid():
    board = []

    for x in range(9):
            board[x].append('+')
    for row in board:
        print (" ".join(row))

def bombBoard():
    bombArray = []
    bombGrid = ['+','-','-']
    for i in range(9):
        for x in range(9):
            anyAdress = random.choice(bombGrid)
            bombArray.append(bombGrid[anyAdress])
    for row in bombGrid:
        print("".join(row))

showGrid()
        
        
        




            
