class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num:
            if num == 1:
                res += 1
                break
            if num % 2 == 0:
                res += 1
            else:
                res += 2
            num = num >> 1
        return res
