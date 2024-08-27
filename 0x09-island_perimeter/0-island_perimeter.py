#!/usr/bin/python3
def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    
    :param grid: List[List[int]], a 2D grid of 0s and 1s
    :return: int, the perimeter of the island
    """
    perimeter = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Start with a perimeter contribution of 4 for the current land cell
                perimeter += 4
                
                # Check the upper cell
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                
                # Check the lower cell
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                
                # Check the left cell
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                
                # Check the right cell
                if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1
    
    return perimeter

