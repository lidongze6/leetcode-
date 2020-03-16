def hollandflag(nums, target):
    """
    给定一个数组和一个数字，
    将所有大于该数字的值放在它的左边，等于的放在中间，大于的放在右边
    """
    less, more = -1, len(nums)
    i = 0
    while i < more:
        if nums[i] < target:
            less += 1
            nums[less], nums[i] = nums[i], nums[less]
            i += 1
        elif nums[i] == target:
            i += 1
        else:
            more -= 1
            nums[more], nums[i] = nums[i], nums[more]


if __name__ == "__main__":
    nums = [4, 2, 5, 7, 9, 1, 3, 5, 2, 5, 8, 10]
    target = 5
    print(nums)
    hollandflag(nums, target)
    print(nums)
