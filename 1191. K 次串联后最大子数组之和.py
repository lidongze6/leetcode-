class Solution:
    def kConcatenationMaxSum(self, arr, k: int) -> int:
        # k==1 按最大子数组和计算
        # k==2 同理
        # k>2 相当于k==2中间夹着k-2个arr，若这arr>0则加上这k-2个，否则舍弃，按k==2计算
        l = len(arr)
        if max(arr) <= 0: return 0
        if l == 1: return k * arr[0] if arr[0] > 0 else 0
        MOD = 10 ** 9 + 7

        def maxsub(arr):
            f = [0] * len(arr)
            f[0] = arr[0]
            res = arr[0]
            for i in range(1, len(arr)):
                f[i] = max(f[i - 1] + arr[i], arr[i])
                res = max(res, f[i])
            return res

        if k == 1: return maxsub(arr)
        if k == 2: return maxsub(arr * 2)
        if k > 2:
            if sum(arr) > 0:
                return (maxsub(arr * 2) + sum(arr) * (k - 2)) % MOD
            else:
                return maxsub(arr * 2) % MOD


nums = [1, -2, 1]
print(Solution().kConcatenationMaxSum(nums, k=5))
