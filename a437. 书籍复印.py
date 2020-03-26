class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """

    def copyBooks(self, pages, k):
        import sys
        # write your code here
        # 如果人数大于书的数量，则一个人负责一本书即可
        if len(pages) < k: return max(pages)

        l = len(pages)
        # f[i][j] 前i个人抄j本书所花的最小时间
        f = [[sys.maxsize] * (l + 1) for i in range(k + 1)]

        for i in range(l + 1):
            if i == 0:
                f[0][i] = 0
            else:
                f[0][i] = sys.maxsize

        for j in range(k + 1):
            f[j][0] = 0

        # 计算前缀和:
        pre_sum = [0] * (l + 1)
        for i in range(1, l + 1):
            pre_sum[i] = pre_sum[i - 1] + pages[i - 1]

        for i in range(1, k + 1):
            for j in range(1, l + 1):
                f[i][j] = min(f[i][j], max(f[i - 1][j], pre_sum[l] - pre_sum[j]))

        return f[-1][-1]


pages=[3,2,4]
k=2
print(Solution().copyBooks(pages,k))
