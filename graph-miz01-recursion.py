def mizdfs_rec(matrix, start, end):
    visit = set()

    def helper(matrix, cur, end):
        if cur[0] == end[0] and cur[1] == end[1]:
            return True
        if matrix[cur[0]][cur[1]] == 1:
            return False

        visit.add(cur)
        for node in neighbor(matrix, cur):
            if node not in visit:
                if helper(matrix, node, end):
                    return True
        return False

    return helper(matrix, start, end)


def neighbor(matrix, node):
    direc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for cur_di in direc:
        tmp = [cur_di[0] + node[0], cur_di[1] + node[1]]
        if 0 <= tmp[0] < len(matrix) and 0 <= tmp[1] < len(matrix[0]):
            yield tuple(tmp)


matrix = [[0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0],
          [1, 1, 0, 1, 1],
          [0, 0, 0, 0, 0]]

start = (0, 0)
end = (4, 4)
print(mizdfs_rec(matrix, start, end))
