def maxAreaOfIsland(grid):
    row, col = len(grid), len(grid[0])
    visit = set()
    res = 0

    def dfs(i, j):
        visit.add((i, j))
        if grid[i][j] != 1:
            return 0
        else:
            count = 1
            dire = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for d in dire:
                tmp = [i + d[0], j + d[1]]
                if tuple(tmp) in visit:
                    continue
                if 0 <= tmp[0] < row and 0 <= tmp[1] < col:
                    count += dfs(tmp[0], tmp[1])
            return count

    for i in range(row):
        for j in range(col):
            if (i, j) not in visit and grid[i][j] == 1:
                res = max(dfs(i, j), res)

    return res


grid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(maxAreaOfIsland(grid))

