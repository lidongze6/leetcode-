class Solution:
    def subarraysDivByK(self, A, K: int) -> int:
        # dict中不记录前缀和的个数了，而是记录前缀和%K后的余数的个数
        dic = {0: 1}
        res = 0
        pre_mod = 0
        for i in range(len(A)):
            pre_mod = (pre_mod + A[i]) % K
            # 如果能在dict中找到相同的pre_mod，说明当前节点前的某个位置的前缀和到当前位置的前缀和间存在若干个K
            if pre_mod in dic:
                res += dic[pre_mod]
            dic[pre_mod] = dic.get(pre_mod, 0) + 1
        return res
