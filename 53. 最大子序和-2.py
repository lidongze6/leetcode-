def maxSubArray(nums):
    # 分治:O(nlogn)
    l, r = 0, len(nums) - 1

    def helper(nums, l, r):
        if l >= r:
            return nums[l]
        mid = l + (r - l) // 2
        left_max = helper(nums, l, mid)
        right_max = helper(nums, mid + 1, r)

        mid_l_max = "-inf"
        tmp_l = 0
        for i in range(mid, l - 1, -1):
            tmp_l += nums[i]
            if tmp_l > float(mid_l_max):
                mid_l_max = tmp_l

        mid_r_max = "-inf"
        tmp_r = 0
        for j in range(mid + 1, r + 1, 1):
            tmp_r += nums[j]
            if tmp_r > float(mid_r_max):
                mid_r_max = tmp_r
        return max(left_max, right_max, mid_r_max + mid_l_max)

    return helper(nums, l, r)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))
