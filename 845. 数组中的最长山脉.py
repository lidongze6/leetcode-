class Solution:
    def longestMountain(self, A) -> int:
        # 先找到山脉顶点，再从顶点左右延伸找到最长山脉。
        if not A: return 0
        res = 0
        for i in range(1, len(A) - 1):
            if A[i] > A[i - 1] and A[i] > A[i + 1]:
                l = r = i
                while l > 0 and A[l] > A[l - 1]:
                    l -= 1
                while r < len(A) - 1 and A[r] > A[r + 1]:
                    r += 1
                res = max(res, r - l + 1)
        return res
