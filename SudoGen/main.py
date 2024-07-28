import random
import numpy as np
import secrets as sc
import random as rnd

# I want to start by making a solver
# Credit Computerphile Python SudokuSolver Youtube video

grid = [[7 ,1, 0,0, 0, 0, 5, 0, 0],
        [0, 0, 0, 7, 1, 5, 0, 2, 0],
        [0, 5, 0, 0, 0, 0, 0, 7, 0],
        [2, 0, 6, 1, 4, 0, 0, 0,0],
        [0, 7, 5, 0, 0 ,2, 0, 4, 0],
        [0, 4, 9, 0, 7, 3, 0, 1, 0],
        [0, 9, 1, 3, 5, 6, 2, 0, 0],
        [0, 8, 7, 4, 2, 0, 0, 3, 0],
        [0, 2, 3, 8, 0, 0, 0, 0, 0]]


def possible(y, x, n):
    global grid

    # This checks  if there is a matching number in the row to n
    for i in range(0, 9):
        if grid[y][i] == n:
            return False

    # This checks if there is a matching number in the column
    for i in range(0, 9):
        if grid[i][x] == n:
            return False

    # This checks if there is a matching number in the grid (3x3)

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        if solve():
                            return True
                        grid[y][x] = 0
                return False

    return True

def print_grid(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(grid[i][j])
            else:
                print(f"{grid[i][j]} ", end="")



def generator():
    global grid
    # NB there no levels to this
    # To make this as random as possible I want to randomly generate a column then use the solve function to fill the rest of the grid
    # This does not work so I looked around and found this solution to populate any 3 diagonal subsquares first

    # First each cell should be zero

    grid = [[0] * 9 for i in range(9)]
    print("")
    print("*****" * 20)
    print("Blank Grid")
    print("*****" * 20)
    print("")
    print(np.matrix(grid))

    # Now to generate I column randomly and add it to grid
    count = 0


    # Loop to fill each diagonal 3x3 subgrid
    for startCoordinate in range(0, 9, 3):
        rndColumn = rnd.sample(range(1, 10), 9)
        count = 0

        # Populating the 3x3 subgrid
        for y in range(3):
            for x in range(3):
                x0 = startCoordinate + x
                y0 = startCoordinate + y
                grid[y0][x0] = rndColumn[count]
                count += 1

    # Print the grid
    print("")
    print("*****"*20)
    print("Generated diagonals")
    print("*****" * 20)
    print("")
    print(np.matrix(grid))



    # Now solve the grid
    print("")
    print("*****"*20)
    print("Solved Grid")
    print("*****" * 20)
    print("")
    if solve():
        print(np.matrix(grid))

    # Now I will remove some numbers at random points in the grid to make the sudoku
    count = 0
    while count <= 35:
        x= rnd.randint(0,8)
        y= rnd.randint(0,8)
        if grid[y][x] != 0 :
            grid[y][x] = 0
            count+=1

    print("")
    print("*****" * 20)
    print("Removed Grid")
    print("*****" * 20)
    print("")

    print(np.matrix(grid))

    print("")
    print("*****" * 20)
    print("Beautified Grid")
    print("*****" * 20)
    print("")

    print_grid(grid)

# Yes so the solver works
# Now for my generator I want it to generate random sudoku puzzles each time I run it ,
def main():
    global grid
    # mySudokuList = [[int for i in range(1, 10)] for j in range(1, 10)]
    # np_array = np.array(mySudokuList)
    generator()
    # print(np.matrix(grid))
    # print(np_array.reshape(9, 9))
    # print(possible(5,7,5))

    # Lets do it
    # Suiiiiii\
    # Column then row


main()
