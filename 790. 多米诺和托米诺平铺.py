class Solution:
    def numTilings(self, N: int) -> int:
        # 序列型DP，f[i]=f[i-1]+f[i-2]+2*f[i-k for k in 3-i]=2*f[i-1]+f[i-3]
        if N == 1: return 1
        if N == 2: return 2
        if N == 3: return 5
        f = [0] * (N + 1)
        f[0]=1
        f[1] = 1
        f[2] = 2
        f[3] = 5
        for i in range(4, N + 1):
            f[i]=2*f[i-1]+f[i-3]
        return f[i]%1000000007

print(Solution().numTilings(10))