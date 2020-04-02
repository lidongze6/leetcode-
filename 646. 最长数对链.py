class Solution:
    def findLongestChain(self, pairs) -> int:
        # 序列型DP，类似于最长上升子序列
        pairs.sort(key=lambda x: x[0])
        l = len(pairs)
        f = [1] * l

        for i in range(1, l):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    f[i] = max(f[i], f[j] + 1)
        return f[l-1]

pairs=[[1,2], [2,3], [3,4]]
print(Solution().findLongestChain(pairs))