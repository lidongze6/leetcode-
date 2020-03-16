def miz02dfs_rec(matrix, start, end):
    visit = set()
    res = []
    road = ""

    def helper(matrix, cur, end, road):
        if cur == end:
            res.append(road)
        visit.add(cur)
        for node, p in neighbor(matrix, cur):
            if node not in visit:
                helper(matrix, node, end, road + p)

    helper(matrix, start, end, road)
    return res


def neighbor(matrix, node):
    road = ["r", "l", "d", "u"]
    direc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for n, cur_di in enumerate(direc):
        tmp = list(node)
        while 0 <= tmp[0] + cur_di[0] < len(matrix) and 0 <= tmp[1] + cur_di[1] < len(matrix[0]) \
                and matrix[tmp[0] + cur_di[0]][tmp[1] + cur_di[1]] != 1:
            tmp[0] += cur_di[0]
            tmp[1] += cur_di[1]
        yield tuple(tmp), road[n]


matrix = [[0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0],
          [1, 1, 0, 1, 1],
          [0, 0, 0, 0, 0]]

start = (0, 0)
end = (1, 4)
print(miz02dfs_rec(matrix, start, end))
