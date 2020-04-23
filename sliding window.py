def sliding_window(nums):
    # 主要是用来处理满足条件的最短子数组或字串
    # 或是判断是否存在满足要求的子数组或字串
    l, r = 0, 0  # 保证区间是左闭右开的
    while r < len(nums):
        c = nums[r]
        r += 1
        # 把c加进去，更新窗口的情况

        while (满足条件):
            # 更新要求的结果，如字串的最短长度
            d = nums[l]
            l += 1
            # 把d从窗口删除，并更新窗口的情况

    return res
