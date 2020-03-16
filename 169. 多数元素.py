def majorityElement(nums):
    # 哈希表：O(n)
    ha = {}
    for i in nums:
        if i not in ha:
            ha[i] = 1
        elif i in ha:
            ha[i] += 1
        if ha[i] > len(nums) // 2:
            return i


nums=[2,2,1,1,1,2,2]
print(majorityElement(nums))
