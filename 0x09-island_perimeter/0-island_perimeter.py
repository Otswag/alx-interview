#!/usr/bin/python3

def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Add 4 to perimeter for each land cell

                # Check adjacent cells
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 if adjacent cell is also land
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
