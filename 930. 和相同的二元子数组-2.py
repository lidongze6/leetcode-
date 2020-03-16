class Solution:
    def numSubarraysWithSum(self, A, S) -> int:
        # 前缀和
        # sum(A[a:b])=pre[b]-pre[a]

        count = {0: 1}
        res = 0
        pre = 0
        for i in range(len(A)):
            pre += A[i]
            if (pre-S) in count:
                res += count[pre-S]
            count[pre] = count.get(pre, 0) + 1

        return res


A = [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0]
S = 2
print(Solution().numSubarraysWithSum(A, S))
