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