import heapq
import sys


def miz03Dij(matrix, start, end):
    visit = set()
    stack = [(0, start)]
    parent = {start: None}
    distance = {start: 0}
    while stack:
        dis, cur = heapq.heappop(stack)
        if cur == end:
            return dis, parent
        visit.add(cur)
        for node, s in neighbor(matrix, cur):
            if node not in visit:
                new_dis = dis + s
                if new_dis < distance.get(node, sys.maxsize):
                    heapq.heappush(stack, (new_dis, node))
                    parent[node] = cur
                    distance[node] = new_dis
    return "impossible"


def neighbor(matrix, node):
    direc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for n, cur_di in enumerate(direc):
        tmp = list(node)
        step = 0
        while 0 <= tmp[0] + cur_di[0] < len(matrix) and 0 <= tmp[1] + cur_di[1] < len(matrix[0]) \
                and matrix[tmp[0] + cur_di[0]][tmp[1] + cur_di[1]] != 1:
            tmp[0] += cur_di[0]
            tmp[1] += cur_di[1]
            step += 1
        yield tuple(tmp), step


matrix = [[0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0],
          [1, 1, 0, 1, 1],
          [0, 0, 0, 0, 0]]

start = (0, 0)
end = (1, 4)
print(miz03Dij(matrix, start, end))
