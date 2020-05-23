class Solution:
    def bestSeqAtIndex(self, height, weight) -> int:
        import bisect
        arr = list(zip(height, weight))
        arr.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, w in arr:
            i = bisect.bisect_left(dp, w)
            if i == len(dp):
                dp.append(w)
            else:
                dp[i] = w
        return len(dp)
