class Solution:
    def readBinaryWatch(self, num: int):
        res = []
        tmp = [0] * 2
        hour = [1, 2, 4, 8]
        minute = [1, 2, 4, 8, 16, 32]

        def helper(res, tmp, index, remain):
            if remain == 0:
                if tmp[1] < 10:
                    res.append(str(tmp[0]) + ":0" + str(tmp[1]))
                else:
                    res.append(str(tmp[0]) + ":" + str(tmp[1]))
                return
            for i in range(index, len(hour + minute)):
                if i < len(hour):
                    if tmp[0] + hour[i] >= 12:
                        continue
                    else:
                        tmp[0] += hour[i]
                        helper(res, tmp, i + 1, remain - 1)
                        tmp[0] -= hour[i]
                else:
                    if tmp[1] + minute[i - len(hour)] >= 60:
                        continue
                    else:
                        tmp[1] += minute[i - len(hour)]
                        helper(res, tmp, i + 1, remain - 1)
                        tmp[1] -= minute[i - len(hour)]

        helper(res, tmp, 0, num)

        return res


print(Solution().readBinaryWatch(2))
