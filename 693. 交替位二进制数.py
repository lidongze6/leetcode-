class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # n向右移一位，若是交替的则结果应全是1
        tmp = n ^ (n >> 1)
        # 全是1的数且上其+1结果为0
        return tmp & (tmp + 1) == 0


print(Solution().hasAlternatingBits(11))
