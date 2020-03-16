class Solution:
    def longestOnes(self, A, K: int) -> int:
        length = len(A)
        if length <= K: return length
        tmp = 0
        res = 0
        l, r = 0, 0
        for r in range(len(A)):
            if A[r] == 0:
                tmp += 1
                res = max(res, r - l)
                while l <= r and tmp > K:
                    if A[l] == 0:
                        tmp -= 1
                    l += 1
        return max(res, r - l + 1)


A = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
K = 3
print(Solution().longestOnes(A, K))
