class Solution:
    def minHeightShelves(self, books, shelf_width: int) -> int:
        l = len(books)
        f = [float("inf")] * (l + 1)
        # f[i]表示前i本书堆成的最小高度
        f[0] = 0
        f[1] = books[0][1]

        for i in range(2, l + 1):
            cur_h = books[i - 1][1]
            cur_width = books[i - 1][0]
            f[i] = cur_h + f[i - 1]
            for j in range(i - 1, 0, -1):
                if cur_width + books[j - 1][0] > shelf_width:
                    break
                cur_width += books[j - 1][0]
                cur_h = max(cur_h, books[j - 1][1])
                f[i] = min(f[i], cur_h + f[j - 1])

        return f[-1]


books = [[7, 3], [8, 7], [2, 7], [2, 5]]
shelf_width = 10
print(Solution().minHeightShelves(books, shelf_width))
