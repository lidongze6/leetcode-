class Solution:
    def maxTurbulenceSize(self, A):
        diff = [1 if A[i] - A[i - 1] > 0 else 0 if A[i] - A[i - 1] == 0 else -1 for i in range(1, len(A))]
        l = 0
        res = 1
        for r in range(0, len(diff)):
            if diff[r] == 0:
                l = r + 1  # l 跳转到第一个不为0的左边界上
                continue
            if r > 0 and diff[r - 1] * diff[r] < 0:  # 当前位置r与前一个位置互为相反数，满足条件
                res = max(res, r - l + 2)
                continue
            elif r > 0 and diff[r - 1] * diff[r] == 0:
                if diff[r] == 0:
                    l = r + 1
                elif diff[r - 1] == 0:
                    continue
            elif r > 0 and diff[r - 1] * diff[r] > 0:
                l = r
        if l == len(diff) - 1:
            res = max(res, 2)
        return res


A = [4, 4,4]
print(Solution().maxTurbulenceSize(A))
