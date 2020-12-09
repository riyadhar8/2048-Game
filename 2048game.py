import random
from copy import deepcopy

## class that creates an object containing the State and all information related to the state
class Game:
    def __init__(self):
        self.board = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]

        self.parent = None
    
    # gives the max value of the board
    def maxBoard(self):
        maxf = 0
        for i in range(4):
            for j in range(4):
                if self.board[i][j] > maxf:
                    maxf = self.board[i][j]
        return maxf

    # gives the total sum of the tiles
    def sumBoard(self):
        sumf = 0
        for i in range(4):
            for j in range(4):
                sumf += self.board[i][j]
        return sumf

    # checks if any of the tiles are empty
    def checkEmpty(self):
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    return True
        return False

    # generates a number at any of the locations
    def randomGenerator(self):
        x = random.randint(0,3)
        y = random.randint(0,3)

        while self.board[x][y] != 0:
            x = random.randint(0,3)
            y = random.randint(0,3)
        
        k = random.randint(0,1)
        if k == 1:
            self.board[x][y] = 4
        else:
            self.board[x][y] = 2
    
    # prints the state of the board
    def printBoard(self):
        maxf = self.maxBoard()
        digits = 0
        while maxf != 0:
            digits = digits + 1
            maxf = maxf//10
        
        for i in range(4):
            for j in range(4):
                b = self.board[i][j]
                d = 0
                if b == 0:
                    d = d + 1
                else:
                    while b != 0:
                        d = d + 1
                        b = b//10
                
                print("|", end = " ")
                for k in range(1,digits-d+1, 1):
                    print("", end = ' ')
                print(self.board[i][j], end = " ")
            print("|", end = '\n')


## function that implements a left move
def moveLeft(game):
    g = Game()
    g.board = deepcopy(game.board)
    g.parent = game
    for i in range(4):
        check = [False, False, False, False]
        for j in range(3,0,-1):
            if g.board[i][j-1] == 0:
                g.board[i][j-1] = g.board[i][j]
                g.board[i][j] = 0
            elif g.board[i][j] == g.board[i][j-1] and check[j] == False:
                g.board[i][j-1] = 2*g.board[i][j-1]
                g.board[i][j] = 0
                check[j-1] = True

    for i in range(4):
        for j in range(3,0,-1):
            if g.board[i][j-1] == 0:
                g.board[i][j-1] = g.board[i][j]
                g.board[i][j] = 0

    return g

## function that implements a right move
def moveRight(game):
    g = Game()
    g.parent = game
    g.board = deepcopy(game.board)
    for i in range(4):
        check = [False, False, False, False]
        for j in range(3):
            if g.board[i][j+1] == 0:
                g.board[i][j+1] = g.board[i][j]
                g.board[i][j] = 0
            elif g.board[i][j] == g.board[i][j+1] and check[j] == False:
                g.board[i][j+1] = 2*g.board[i][j+1]
                g.board[i][j] = 0
                check[j+1] = True

    for i in range(4):
        for j in range(3):
            if g.board[i][j+1] == 0:
                g.board[i][j+1] = g.board[i][j];
                g.board[i][j] = 0

    return g

## function that implements an up move
def moveUp(game):
    g = Game()
    g.parent = game
    g.board = deepcopy(game.board)

    for j in range(4):
        check = [False, False, False, False]
        for i in range(3,0,-1):
            if g.board[i-1][j] == 0:
                g.board[i-1][j] = g.board[i][j]
                g.board[i][j] = 0
            elif g.board[i][j] == g.board[i-1][j] and check[i] == False:
                g.board[i-1][j] = 2*g.board[i-1][j]
                g.board[i][j] = 0
                check[i-1] = True

    for j in range(4):
        for i in range(3,0,-1):
            if g.board[i-1][j] == 0:
                g.board[i-1][j] = g.board[i][j]
                g.board[i][j] = 0

    return g

## function that implements a down move
def moveDown(game):
    g = Game()
    g.parent = game
    g.board = deepcopy(game.board)

    for j in range(4):
        check = [False, False, False, False]
        for i in range(3):
            if g.board[i+1][j] == 0:
                g.board[i+1][j] = g.board[i][j]
                g.board[i][j] = 0

            elif g.board[i+1][j] == g.board[i][j] and check[i] == False:
                g.board[i+1][j] = 2*g.board[i+1][j]
                g.board[i][j] = 0
                check[i+1] = True

    for j in range(4):
        for i in range(3):
            if g.board[i+1][j] == 0:
                g.board[i+1][j] = g.board[i][j]
                g.board[i][j] = 0

    return g

## function that provides a hint to the user and returns the move, the new state and the maximum value possible after that move
def giveHint(game):
    g1 = moveLeft(game)
    g2 = moveRight(game)
    g3 = moveUp(game)
    g4 = moveDown(game)

    maxval = 0
    char = 'h'
    if g1.maxBoard() > maxval:
        maxval = g1.maxBoard()
        char = 'l'
    if g2.maxBoard() > maxval:
        maxval = g2.maxBoard()
        char = 'r'
    if g3.maxBoard() > maxval:
        maxval = g3.maxBoard()
        char = 'u'
    if g4.maxBoard() > maxval:
        maxval = g4.maxBoard()
        char = 'd'

    if char == 'l':
        del g2, g3, g4
        return char, g1, maxval
    if char == 'r':
        del g1, g3, g4
        return char, g2, maxval
    if char == 'u':
        del g1, g2, g4
        return char, g3, maxval
    if char == 'd':
        del g1, g2, g3
        return char, g4, maxval

    return None, None, 0

def main():
    game = Game()
    game.randomGenerator()
    game.randomGenerator()
    print("Welcome to 2048!", end = '\n\n')
    print("To play, use these moves: u for up, d for down, l for left, r for right, s for sum, m for max, h for hint, b for backtrack and q for quit. Good luck!", end = '\n\n')
    game.printBoard()
    print("", end = '\n')
    
    c = input("Enter your first move: ")

    while c:
        if c == 'q':
            break
        
        if game.maxBoard() == 2048:
            break

        if not game.checkEmpty:
            break

        if c == 'l':
            game = moveLeft(game)
            game.randomGenerator()
            game.printBoard()
            print("", end = '\n')

        elif c == 'r':
            game = moveRight(game)
            game.randomGenerator()
            game.printBoard()
            print("", end = '\n')

        elif c == 'u':
            game = moveUp(game)
            game.randomGenerator()
            game.printBoard()
            print("", end = '\n')

        elif c == 'd':
            game = moveDown(game)
            game.randomGenerator()
            game.printBoard()
            print("", end = '\n')

        elif c == 'b':
            if game.parent == None:
                print("This is the first state of the board, no option to backtrack.", end = '\n\n')
            else:
                game = game.parent
                game.printBoard()
                print("", end = '\n')
                c = input("Enter your next move: ")
                continue

        elif c == 's':
            print("Your total upto now is:", game.sumBoard(), sep = " ", end = '\n\n')

        elif c == 'm':
            print("Your max upto now is:", game.maxBoard(), sep = " ", end = '\n\n')

        # user has the option to choose the hint or not choose the hint
        elif c == 'h':
            move, g, maxval = giveHint(game)
            print("Best max value will be achieved in the move", move, sep = " ", end = '\n')
            print("The max value achieved would be", maxval, sep = " ", end = '\n\n')
            take = input("Do you want to pick this move y or no: ")
            if take == 'y':
                game = g
                game.randomGenerator()
                game.printBoard()
                print("", end = '\n')
            
            else:
                del g
        
        else:
            print("Invalid move. Valid moves are u for up, d for down, l for left, r for right, s for sum, m for max, h for hint, b for backtrack and q for quit. Try again!", end = '\n\n')

        c = input("Enter your next move: ")

    print("Thank you for playing!", end = '\n')

    if game.maxBoard() == 2048:
        print("Your max value is 2048! You have won!!", end = '\n')

    if not game.checkEmpty():
        print("You have lost with the total as", game.maxBoard(), sep = " ", end = ".\n")

    if c == 'q':
        print("You have chosen to quit with the max score of", game.maxBoard(), sep = " ", end = ".\n")
        
    return None


if __name__=='__main__':
    main()
