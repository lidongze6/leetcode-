def canPartitionKSubsets(nums, k):
    # 为空或不够分
    if not nums or len(nums) < k:
        return False

    # 不能整除
    avg, mod = divmod(sum(nums), k)
    if mod: return False

    # 倒序排列
    nums.sort(reverse=True)

    # 有超过目标的元素
    if nums[0] > avg:
        return False
    used = set()  # 记录已使用的数的索引

    def dfs(k, start, tmpSum):
        """
        :param k: 当前还需要凑的avg个数，
        :param start: 当前从哪个数开始考虑
        :param tmpSum: 当前已凑够的和
        :return: True or False
        """

        if tmpSum == avg:  # 如果已凑满一个
            return dfs(k - 1, 0, 0)  # 那么从最大数重新开始考虑，凑下一个

        if k == 1:  # 只剩最后一个，那么剩下的没使用的数加起来肯定凑满,这是因为在前面main函数中、
            # 已经判断了如果有余数不能被均分，因而当k==1的时候证明用过的数字都可以组成target、
            # 了，那么剩下来的一定可以组成了
            return True

        for i in range(start, len(nums)):  # 优先用大的数的凑
            if i not in used and nums[i] + tmpSum <= avg:  # 如果该数未使用并且可以用来凑
                used.add(i)  # 使用该数
                if dfs(k, i + 1, nums[i] + tmpSum):  # 继续用比该数小的数来凑
                    return True
                used.remove(i)  # 没有得到可用方案，则换个数来凑
        return False

    return dfs(k, 0, 0)


nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
print(canPartitionKSubsets(nums, k))
