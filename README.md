

---


# SudoGen (A Sudoku Generator)

This Python program generates and solves Sudoku puzzles. It uses a combination of random number generation and a backtracking algorithm to create a valid Sudoku grid and then remove some numbers to form the puzzle.
![SudoGen Logo](https://github.com/user-attachments/assets/e39e03a9-fa88-4c81-ab94-9bb0eccd0be7)
## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
  - [possible](#possible)
  - [solve](#solve)
  - [print_grid](#print_grid)
  - [generator](#generator)
  - [main](#main)
- [Examples](#examples)
- [Credits](#credits)

## Installation
To run this program, you'll need to have Python installed on your system. Additionally, you need to install the `numpy` library. You can install it using `pip`:

```sh
pip install numpy
```

## Usage
To generate and solve a Sudoku puzzle, simply run the program. The program will print the steps taken to generate the grid, solve it, and finally create a puzzle by removing some numbers.

```sh
python sudoku_generator.py
```

## Functions

### `possible(y, x, n)`
Checks if it's possible to place a number `n` in the cell located at row `y` and column `x`.

**Parameters:**
- `y` (int): Row index.
- `x` (int): Column index.
- `n` (int): Number to be placed (1-9).

**Returns:**
- `bool`: `True` if the number can be placed, `False` otherwise.

### `solve()`
Solves the Sudoku grid using a backtracking algorithm. It recursively tries to fill the grid with valid numbers.

**Returns:**
- `bool`: `True` if the grid is successfully solved, `False` otherwise.

### `print_grid(grid)`
Prints the Sudoku grid in a formatted manner with lines separating the 3x3 subgrids.

**Parameters:**
- `grid` (list): The 9x9 Sudoku grid.

### `generator()`
Generates a Sudoku puzzle by:
1. Initializing an empty grid.
2. Filling the diagonal 3x3 subgrids with random numbers.
3. Solving the grid to ensure it's valid.
4. Removing random numbers to create the puzzle.

### `main()`
The main function that runs the Sudoku generator.

## Examples

When you run the program, it will print the following steps:

1. **Blank Grid:**
   ```
   [[0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]]
   ```

2. **Generated Diagonals:**
   ```
   [[4 1 3 0 0 0 0 0 0]
    [9 2 5 0 0 0 0 0 0]
    [8 7 6 0 0 0 0 0 0]
    [0 0 0 1 6 7 0 0 0]
    [0 0 0 9 2 5 0 0 0]
    [0 0 0 3 4 8 0 0 0]
    [0 0 0 0 0 0 2 9 8]
    [0 0 0 0 0 0 1 4 5]
    [0 0 0 0 0 0 3 6 7]]
   ```

3. **Solved Grid:**
   ```
   [[4 1 3 8 9 2 5 7 6]
    [9 2 5 7 6 1 4 8 3]
    [8 7 6 5 3 4 9 1 2]
    [3 4 8 1 6 7 2 5 9]
    [7 6 9 4 2 5 8 3 1]
    [1 5 2 3 4 8 7 6 9]
    [6 3 4 2 1 9 2 9 8]
    [2 8 1 6 7 3 1 4 5]
    [5 9 7 9 8 6 3 6 7]]
   ```

4. **Removed Grid:**
   ```
   [[4 1 3 0 0 0 5 7 6]
    [9 0 5 7 6 1 4 0 0]
    [8 0 0 5 0 4 9 1 2]
    [3 4 0 1 0 7 2 0 9]
    [7 6 9 4 0 5 8 3 0]
    [1 0 2 0 0 8 7 6 9]
    [6 0 4 0 1 0 2 0 8]
    [2 0 1 6 7 3 0 0 5]
    [5 0 0 9 8 0 0 6 7]]
   ```

5. **Beautified Grid:**
   ```
   4 1 3  | 0 0 0  | 5 7 6
   9 0 5  | 7 6 1  | 4 0 0
   8 0 0  | 5 0 4  | 9 1 2
   ---------------------
   3 4 0  | 1 0 7  | 2 0 9
   7 6 9  | 4 0 5  | 8 3 0
   1 0 2  | 0 0 8  | 7 6 9
   ---------------------
   6 0 4  | 0 1 0  | 2 0 8
   2 0 1  | 6 7 3  | 0 0 5
   5 0 0  | 9 8 0  | 0 6 7
   ```

## Credits
- Inspired by the Computerphile Python Sudoku Solver YouTube video.
- `numpy` library for matrix representation.

---

