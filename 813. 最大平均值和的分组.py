class Solution:
    def largestSumOfAverages(self, A, K: int):
        if K == 1:
            return sum(A)/len(A)
        l = len(A)
        f = [[0.0] * (K+1) for _ in range(l)]
        # f[i][j]表示到第i个数字组成j+1组的最大值

        f[0][1]=A[0]
        for i in range(1,l):
            f[i][1] = sum(A[:i+1])/(i+1)

        for k in range(2, K+1):
            for i in range(k-1, l):
                for j in range(i):
                    f[i][k] = max(f[i][k], f[j][k-1] + (sum(A[j+1:i+1])) / (i - j))
        return f


A = [1,2]
K = 1
print(Solution().largestSumOfAverages(A, K))
