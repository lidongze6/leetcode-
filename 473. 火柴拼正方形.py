class Solution:
    def makesquare(self, nums):
        # 通过但超时
        nums.sort(reverse=True)
        if len(nums) < 4 or sum(nums) % 4 != 0:
            return False
        lengh = sum(nums) // 4

        def dfs(tmp, count, nums):
            if count == 3 and sum(nums) == lengh: return True
            for i in range(len(nums)):
                if nums[-1] + tmp > lengh: break
                if tmp + nums[i] < lengh and dfs(tmp + nums[i], count, nums[:i] + nums[i + 1:]):
                    return True
                elif tmp + nums[i] == lengh and dfs(0, count + 1, nums[:i] + nums[i + 1:]):
                    return True
            return False

        return dfs(0, 0, nums)


nums = [6035753, 3826635, 922363, 6104805, 1189018, 6365253, 364948, 2725801, 5577769, 7857734, 2860709, 9554210,
        4883540, 8712121, 3545089]
s = Solution()
print(s.makesquare(nums))
