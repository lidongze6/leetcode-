class Solution:
    def canJump(self, nums) -> bool:
        # 贪心
        l = len(nums)
        if l <= 1: return True
        f = [0] * l  # f[i]表示当前位置所能跳跃的最远距离

        f[0] = nums[0]
        for i in range(1, l):
            if i <= f[i - 1]:  # 说明能跳到当前位置
                f[i] = max(i + nums[i], f[i - 1])
            else:
                f[i] = f[i - 1]
            if f[i] >= l - 1:
                return True
        return False
