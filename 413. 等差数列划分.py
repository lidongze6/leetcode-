class Solution:
    def numberOfArithmeticSlices(self, A):
        l = len(A)
        if l <= 2: return 0
        diff = [0]
        for i in range(1, l):
            diff.append(A[i] - A[i - 1])

        f = [0] * l  # f[i]表示以i结尾的数字组成的等差数列的个数
                    # 若连续三个数的差相等，则f[i]=f[i-1]+1

        for i in range(2, l):
            if diff[i] == diff[i - 1]:
                f[i] += f[i - 1] + 1
        return sum(f)


A = [1, 2, 3, 4]
print(Solution().numberOfArithmeticSlices(A))
