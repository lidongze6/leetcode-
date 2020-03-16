class Solution:
    def networkDelayTime(self, times, N, K):
        import heapq
        from collections import defaultdict
        dict1 = defaultdict(list)
        for t in times:
            dict1[t[0]].append([t[2], t[1]])
        dis = [1000] * (N + 1)
        dis[K] = 0
        stack = []
        heapq.heappush(stack, [0, K])
        visit = set()
        while stack:
            time, cur = heapq.heappop(stack)
            if cur not in visit:
                visit.add(cur)
            for t, node in dict1[cur]:
                if time + t < dis[node]:
                    dis[node] = time + t
                    stack.append([dis[node], node])
        return max(dis[1:]) if N == len(visit) else -1


times = [[1, 2, 1], [2, 3, 2], [1, 3, 4]]
N = 3
K = 1
s = Solution()
print(s.networkDelayTime(times, N, K))
