class Solution:
    def findContinuousSequence(self, target: int):
        import math
        n = (target + 1) // 2
        res = []
        for i in range(1, n):
            tmp = (math.sqrt(4 * i * i + 1 - 4 * i + 8 * target) + (1 - 2 * i))
            k, ret = divmod(tmp, 2)
            if ret == 0 and 1 < k < target:
                res.append([x for x in range(i, i+int(k))])

        return res


print(Solution().findContinuousSequence(15))
