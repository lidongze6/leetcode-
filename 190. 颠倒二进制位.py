class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        power = 31
        while n:
            res += (1 & n) << power
            n = n >> 1
            power -= 1
        return res
