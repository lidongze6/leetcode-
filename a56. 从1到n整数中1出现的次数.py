class Solution(object):
    def numberOf1Between1AndN_Solution(self, n):
        if n == 0: return 0
        if n == 1: return 1
        f = [0] * (1 + n)
        f[1] = 1
        for i in range(2, 1 + n):
            if i % 10 == 1:
                f[i] = f[i // 10] + 1
            else:
                f[i] = f[i // 10]

        return sum(f)


print(Solution().numberOf1Between1AndN_Solution(123456789))
