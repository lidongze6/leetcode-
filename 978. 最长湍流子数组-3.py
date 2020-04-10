class Solution:
    def maxTurbulenceSize(self, A):
        l = len(A)
        if l<=1:return l
        up = [1] * l
        down = [1] * l
        res=0
        for i in range(1, l):
            if A[i] > A[i - 1]:
                up[i] = max(up[i], down[i - 1] + 1)
            elif A[i] < A[i - 1]:
                down[i] = max(down[i], up[i-1] + 1)

            res=max(res,up[i],down[i])

        return res

A=[9, 4, 2, 10, 7, 8, 8, 1, 9]
print(Solution().maxTurbulenceSize(A))