class Solution:
    def jump(self, nums) -> int:
        # dfs+记忆化，超时
        dic = dict()
        l = len(nums) - 1

        def dfs(cur):
            if cur == 0:
                return 0
            if cur in dic:
                return dic[cur]
            tmp = float("inf")
            for i in range(cur):
                if i + nums[i] >= cur:
                    tmp = min(tmp, dfs(i) + 1)
            dic[cur] = tmp
            return tmp

        return dfs(l)
