class Solution:
    def singleNumber(self, nums) -> int:
        # 本题难点在于时间复杂度O(n),空间复杂度要求时O(1)
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1
                num >>= 1
        res = counts[31] % 3
        for i in range(1, 32):
            res <<= 1
            res |= counts[31 - i] % 3

        return res - 2 ** 32 if res > 2 ** 31 - 1 else res


nums = [-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]
print(Solution().singleNumber(nums))
