class Solution:
    def maximumSum(self, arr) -> int:
        l = len(arr)
        if l == 1: return arr[0]
        Y = [float("inf")] * l   # 删除一次的
        N = [float("inf")] * l   # 没有删除的
        Y[0] = 0
        N[0] = arr[0]
        res = float("-inf")
        for i in range(1, l):
            Y[i] = max(Y[i - 1] + arr[i], N[i - 1]) # 前面的删除了一个+本次的；前面的没删除，删除本次的，
            N[i] = max(N[i - 1] + arr[i], arr[i])   # 前面没删除的+本次的；前面没删除但是值小于0，则舍弃前面的，从当前开始
                                                    # 类似于leetcode 53 最大子序和
            res = max(res, Y[i], N[i])

        return res

arr=[-1,-1,-1,-1]
print(Solution().maximumSum(arr))