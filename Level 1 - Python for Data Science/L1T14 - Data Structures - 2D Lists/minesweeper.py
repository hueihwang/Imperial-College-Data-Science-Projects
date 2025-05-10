def count_adjacent_mines(grid, row, col):
    
    rows = len(grid)
    cols = len(grid[0])
    mine_count = 0

    directions = [
        (-1, -1), (-1, 0), (-1, 1),  
        (0, -1),         (0, 1), 
        (1, -1), (1, 0), (1, 1)       
    ]

    for dr, dc in directions:
        row_1, col_1 = row + dr, col + dc
        if 0 <= row_1 < rows and 0 <= col_1 < cols: 
            if grid[row_1][col_1] == "#":
                mine_count += 1

    return str(mine_count)


def minesweeper(grid):
   
    new_grid = []

    for row_idx, row in enumerate(grid):
        row_1 = []
        for col_idx, cell in enumerate(row):
            if cell == "#":
                row_1.append("#")
            else:
                row_1.append(count_adjacent_mines(grid, row_idx, col_idx))
        new_grid.append(row_1)

    return new_grid

input_grid = [["-", "-", "-", "#", "#"],["-", "#", "-", "-", "-"],["-", "-", "#", "-", "-"],["-", "#", "#", "-", "-"],["-", "-", "-", "-", "-"]]

output_grid = minesweeper(input_grid)
for row in output_grid:
    print(row)
