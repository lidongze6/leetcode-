class Solution:
    def maxJumps(self, arr, d: int) -> int:
        le = len(arr)
        dp = [1] * le
        con = [[i, arr[i]] for i in range(le)]
        con.sort(key=lambda x: x[1])

        for idx, height in con:
            for l in range(idx - 1, max(idx - d, 0) - 1, -1):
                if arr[l] >= height:  # 中途有高于当前台阶的，后面的都跳不到了
                    break
                dp[idx] = max(dp[idx], dp[l] + 1)

            for r in range(idx + 1, min(idx + d + 1, le)):
                if arr[r] >= height:  # 中途有高于当前台阶的，后面的都跳不到了
                    break
                dp[idx] = max(dp[idx], dp[r] + 1)
        return max(dp)


arr = [6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12]
d = 2
print(Solution().maxJumps(arr, d))
