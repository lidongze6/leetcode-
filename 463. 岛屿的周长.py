def islandPerimeter(grid):
    res = 0
    # 现在grid四周填0
    row, col = len(grid), len(grid[0])
    for i in range(row):
        grid[i].insert(col, 0)
        grid[i].insert(0, 0)
    grid.insert(row, [0] * (col + 2))
    grid.insert(0, [0] * (col + 2))

    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if grid[i][j] == 1:
                res += [grid[i - 1][j], grid[i + 1][j], grid[i][j - 1], grid[i][j + 1]].count(0)
    return res
