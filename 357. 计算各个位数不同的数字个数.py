class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 10  # 0-9
        f = [0] * (n + 1)  # n位有多少个不同的数字
        f[0] = 1
        f[1] = 10
        mul = 9
        for i in range(2, min(n + 1, 10)):
            mul*=(11-i)
            f[i]=f[i-1]+mul

        return f[-1]


print(Solution().countNumbersWithUniqueDigits(3))
