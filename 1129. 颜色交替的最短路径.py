class Solution:
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        from collections import defaultdict
        from collections import deque
        connenction = defaultdict(list)
        for s, v in red_edges:
            connenction[s].append([v, 1])
        for q, p in blue_edges:
            connenction[q].append([p, -1])
        res = [400] * n
        res[0] = 0

        def bfs(node):
            stack = deque()
            visit = set()
            stack.append([0, 0, 0])
            while stack:
                cur, step, cur_color = stack.popleft()
                if cur == node: return step
                if step < res[cur]:
                    res[cur] = step
                for i, color in connenction[cur]:
                    if (cur, i, color) not in visit and color * cur_color != 1:
                        visit.add((cur, i, color))
                        stack.append([i, step + 1, color])
            return -1

        for i in range(1, n):
            res[i] = bfs(i)
        return res


n = 5
red_edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
blue_edges = [[1, 2], [2, 3], [3, 1]]

s = Solution()
print(s.shortestAlternatingPaths(n, red_edges, blue_edges))
