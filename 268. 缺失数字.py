class Solution:
    def missingNumber(self, nums) -> int:
        # 位运算
        # 所以任一数字，异或自己肯定等于0。 此外异或运算满足交换律A^B^C = A^C^B
        # 且用异或刚好可以得出缺失的数字。
        res = 0
        for i, n in enumerate(nums):
            res ^= i ^ n
        res ^= len(nums)
        return res
