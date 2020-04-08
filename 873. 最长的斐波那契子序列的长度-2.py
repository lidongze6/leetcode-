class Solution:
    def lenLongestFibSubseq(self, A) -> int:
        l = len(A)
        if l < 2: return 0
        f = [[2] * l for i in range(l)]
        ind = {x: i for i, x in enumerate(A)}
        res = 2
        for i in range(l - 1):
            for k in range(i + 1, l):
                tmp = A[k] - A[i]
                if tmp in ind:
                    if ind[tmp] >= i:
                        break
                    f[i][k] = f[ind[tmp]][i] + 1
                res = max(res, f[i][k])
        return res if res > 2 else 0


A = [1, 2, 3, 4, 5, 6, 7, 8]
print(Solution().lenLongestFibSubseq(A))
