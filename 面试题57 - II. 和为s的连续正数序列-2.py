class Solution:
    def findContinuousSequence(self, target: int):
        res = []
        l, r = 1, 2
        tmp = l + r
        while r <= ((target+1) // 2):
            if tmp < target:
                r += 1
                tmp += r
            elif tmp > target:
                tmp -= l
                l += 1
            elif tmp == target:
                res.append([i for i in range(l, r + 1)])
                tmp -= l
                l += 1
                r += 1
                tmp += r
        return res


print(Solution().findContinuousSequence(15))
