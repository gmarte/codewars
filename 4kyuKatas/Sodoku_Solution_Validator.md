# Sodoku Solution Validator

[Codewars Kata KYU - 4](https://www.codewars.com/kata/529bf0e9bdf7657179000008/python)

Join [CodeWars](www.codewars.com/r/v0KX6w) and follow [me](https://www.codewars.com/users/gmarte)!

## Sudoku Background
Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
(More info at: http://en.wikipedia.org/wiki/Sudoku)

## Sudoku Solution Validator
Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

Examples
```
validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]); // => true
```

```
validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2], 
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
]); // => false
```

### Given Code
```python
def valid_solution(board):
```
### Solution

```python
import numpy as np

def valid_solution(board):
    result = True
    compareList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    zerocount = [x for x in board if 0 in x or len(x) != 9 or len(board) != 9]
    if False in zerocount:
        return False
    # 3x3
    newboard = get_subgrids(board)    
    compareBool = [True if sorted(x) == compareList else False for x in board]
    if False in compareBool:
        return False
    board = list(map(list, zip(*board)))[::-1]
    compareBool = [True if sorted(x) == compareList else False for x in board]
    if False in compareBool:
        return False
    treeBytree = [True if sorted(
        list(x)) == compareList else False for x in newboard]
    if False in treeBytree:
        return False
    return result

def get_subgrids(grid):
    subgrids = []
    for box_i in range(3):
        for box_j in range(3):
            subgrid = []
            for i in range(3):
                for j in range(3):
                    subgrid.append(grid[3*box_i + i][3*box_j + j])
            subgrids.append(subgrid)
    return np.array(subgrids)
```    