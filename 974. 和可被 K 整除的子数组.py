class Solution:
    def subarraysDivByK(self, A, K: int) -> int:
        # 超时，Key太多了
        dic = {0: 1}
        pre_sum = 0
        res = 0
        for i in range(len(A)):
            pre_sum += A[i]
            for m in dic.keys():
                if (pre_sum - m) % K == 0:
                    res += dic[m]
            dic[pre_sum] = dic.get(pre_sum, 0) + 1

        return res


A = [4, 5, 0, -2, -3, 1]
K = 5
print(Solution().subarraysDivByK(A, K))
