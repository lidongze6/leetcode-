class Solution:
    def jump(self, nums) -> int:
        # 贪心
        count = 0
        start, end = 0, 0  # 每一次跳跃的起点范围[start, end]
        max_pos = 0
        # 循环起跳，直到起跳范围达到或超过数组长度
        while end < len(nums) - 1:
            # 计算每轮跳跃能达到的最大索引位置
            for i in range(start, end + 1):
                max_pos = max(max_pos, i + nums[i])
            # 更新下一次起跳的取值范围，并将起跳数加一
            start = end + 1
            end = max_pos
            count += 1
        return count

nums = [2,3,0,1,4]
print(Solution().jump(nums))
