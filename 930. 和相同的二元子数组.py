class Solution:
    def numSubarraysWithSum(self, A, S: int):
        # 官方解题，暂时没看懂
        indexes = [-1] + [ix for ix, v in enumerate(A) if v] + [len(A)]
        ans = 0

        if S == 0:
            for i in range(len(indexes) - 1):
                # w: number of zeros between two consecutive ones
                w = indexes[i + 1] - indexes[i] - 1
                ans += w * (w + 1) / 2
            return ans

        for i in range(1, len(indexes) - S):
            j = i + S - 1
            left = indexes[i] - indexes[i - 1]
            right = indexes[j + 1] - indexes[j]
            ans += left * right
        return ans





A = [0,0,1,0,0,0,1,0,0,1,0]
S = 2
print(Solution().numSubarraysWithSum(A,S))