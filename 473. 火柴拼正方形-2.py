class Solution:
    def makesquare(self, nums):
        # 超时，貌似要用DP
        nums.sort(reverse=True)
        if len(nums) < 4 or sum(nums) % 4 != 0:
            return False
        lengh = sum(nums) // 4
        res = [0 for _ in range(4)]
        visit = [False for _ in range(len(nums))]
        return self.dfs(res, lengh, 0, nums, 0, visit)

    def dfs(self, res, lengh, index, nums, tmpsum, visit):
        if index == 4:
            return True
        if tmpsum == lengh:
            return self.dfs(res, lengh, index + 1, nums, 0, visit)
        for i in range(len(nums)):
            if visit[i] or tmpsum + nums[i] > lengh:
                continue
            if i > 0 and nums[i - 1] == nums[i] and visit[i - 1] == False:
                continue
            else:
                visit[i] = True
                if self.dfs(res, lengh, index, nums, tmpsum + nums[i], visit):
                    return True
                else:
                    visit[i] = False
        return False


nums = [6035753, 3826635, 922363, 6104805, 1189018, 6365253, 364948, 2725801, 5577769, 7857734, 2860709, 9554210,
        4883540, 8712121, 3545089]
s = Solution()
print(s.makesquare(nums))
