class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, K: int) -> int:
        # DP
        from collections import defaultdict
        connection = defaultdict(list)
        f = [[float("inf")] * (K + 2) for i in range(n)]
        # f[i][k]表示从src到i至少需要k站所花费的最少费用
        for u, v, w in flights:
            connection[v].append([u, w])
            if u == src:
                f[v][1] = w  # scr到v乘坐一次花费为w
        for j in range(K+2): # 从src到src，乘坐多少此都是0花费
            f[src][j]=0
        for k in range(2,K+2):
            for i in range(n):
                f[i][k]=f[i][k-1]
                for u,w in connection[i]:
                    f[i][k]=min(f[i][k],f[u][k-1]+w)
        #return f
        return f[dst][K+1] if f[dst][K+1] !=float("inf") else -1

n = 10
edges = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
src = 6
dst = 0
k = 7
print(Solution().findCheapestPrice(n, edges, src, dst, k))
