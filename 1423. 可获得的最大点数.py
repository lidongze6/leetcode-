class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        # 滑动窗口
        # 寻找连续的len(cardpoints)-k个数使得它们的值最小
        if k >= len(cardPoints):
            return sum(cardPoints)

        l, r = 0, len(cardPoints) - k - 1
        tmp = sum(cardPoints[l:r])
        res = float("inf")
        while r < len(cardPoints):
            tmp += cardPoints[r]
            r += 1

            res = min(res, tmp)

            tmp -= cardPoints[l]
            l += 1
        return sum(cardPoints) - res
