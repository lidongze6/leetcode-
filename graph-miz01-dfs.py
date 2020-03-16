def mizdfs(matrix, start, end):
    visit = set()
    stack = [start]
    while stack:
        cur = stack.pop()
        visit.add(cur)
        if cur == end:
            return True
        for node in neighbor(matrix, cur):
            if matrix[node[0]][node[1]] == 1:
                continue
            if node not in visit:
                stack.append(node)
    return False


def neighbor(matrix, node):
    direc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for cur_di in direc:
        tmp = [cur_di[0] + node[0], cur_di[1] + node[1]]
        if 0 <= tmp[0] < len(matrix) and 0 <= tmp[1] < len(matrix[0]):
            yield tuple(tmp)


matrix = [[0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0],
          [1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0]]

start = (0, 0)
end = (4, 4)
print(mizdfs(matrix, start, end))