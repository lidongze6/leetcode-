class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 序列型DP
        f = [0] * (target + 1)
        f[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    f[i] += f[i - num]
        return f[-1]
