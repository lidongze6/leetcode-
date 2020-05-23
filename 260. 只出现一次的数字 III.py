class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a = 0
        for n in nums:
            a ^= n

        mask = a & (-a)
        res = [0, 0]
        for n in nums:
            if n & mask:
                res[0] ^= n
            else:
                res[1] ^= n
        return res