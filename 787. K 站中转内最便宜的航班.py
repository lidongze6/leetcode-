class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        from collections import defaultdict
        import heapq
        connection = defaultdict(list)
        for u, v, w in flights:
            connection[u].append([w, v])
        stack = []
        heapq.heappush(stack, [0, src, 0])
        while stack:
            cost, cur, step = heapq.heappop(stack)
            if step > K+1:
                continue
            elif cur == dst and step <= K+1:
                return cost
            for new_cost, new_node in connection[cur]:
                heapq.heappush(stack, [cost + new_cost, new_node, step + 1])
        return -1


n = 4
edges = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
k = 1
s = Solution()
print(s.findCheapestPrice(n, edges, src, dst, k))
