class Solution:
    def lenLongestFibSubseq(self, A):
        l = len(A)
        s = set(A)
        ans = 2
        for i in range(1, l):
            for j in range(i):
                res = 2
                pre = A[j]
                fow = A[i]
                while pre + fow in s:
                    pre, fow = fow, pre + fow
                    res += 1
                ans = max(ans, res)

        return ans if ans > 2 else 0


A = [1, 2, 3, 4, 5, 6, 7, 8]
print(Solution().lenLongestFibSubseq(A))
