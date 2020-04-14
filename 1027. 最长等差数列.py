class Solution:
    def longestArithSeqLength(self, A) -> int:
        # 提供了一种新方法，在不知道边界的情况下可以使用dict去存储出现的情况
        f = [{} for i in range(len(A))]
        res = 1
        for i in range(1, len(A)):
            for j in range(i):
                f[i][A[i] - A[j]] = f[j].get(A[i] - A[j], 1) + 1
                res = max(res, f[i][A[i] - A[j]])

        return res
