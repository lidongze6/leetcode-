class Solution:
    def eventualSafeNodes(self, graph):
        # 拓扑排序，因为是找没有出边的点，所以要维护一个出度表和一个逆邻接表
        from collections import deque
        from collections import defaultdict
        if len(graph) == 1: return [0]
        res = []
        connect = defaultdict(list)
        indegree = dict()
        stack = deque()
        for i in range(len(graph)):
            for j in graph[i]:
                connect[j].append(i)
            indegree[i] = len(graph[i])
            if indegree[i] == 0:
                stack.append(i)
                res.append(i)
        while stack:
            curnode = stack.popleft()
            for i in connect[curnode]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    stack.append(i)
                    res.append(i)

        return res


graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
s = Solution()
print(s.eventualSafeNodes(graph))
