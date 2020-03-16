class Solution:
    def maxTurbulenceSize(self, A) -> int:
        # 别人的，自己写的太垃圾了
        ans, l = 1, 0
        for r in range(1, len(A)):
            curr = A[r - 1] - A[r]
            if r == len(A) - 1 or curr * (A[r] - A[r + 1]) >= 0:
                if curr != 0:
                    ans = max(ans, r - l + 1)
                l = r

        return ans


A=[5,4,2,10,7,8,8,1,9]
print(Solution().maxTurbulenceSize(A))