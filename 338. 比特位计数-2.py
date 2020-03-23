class Solution:
    def countBits(self, num: int) -> List[int]:
        # 奇数的二进制中1的个数=它上一位偶数的二进制中1的个数+1
        # 如：3=(11),2=(10);​13=(1101),12=(1100)
        # 偶数中二进制1的个数等于这个偶数除以2后的数二进制1的个数。
        # 如：10=(1010);(1010)<<1=(10100)=20

        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            if (i % 2 == 1):
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i // 2]
        return dp
