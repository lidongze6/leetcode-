class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # 先统计个数字的多少，然后就和打家劫舍一样了
        if not nums: return 0
        from collections import Counter
        c = Counter(nums)
        mi, ma = min(nums), max(nums)

        f = [0] * (ma - mi + 1)

        Y, N = c[mi] * mi, 0
        for i in range(1, ma - mi + 1):
            Y, N = N + c[mi + i] * (mi + i), max(Y, N)

        return max(Y, N)