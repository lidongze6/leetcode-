nums = [[21, 3, 45, 130], [77, 71, 25, 86], [60, 101, 103, 5], [8, 17, 68, 66]]

pre_sum = [[0 for _ in range(len(nums[0]) + 1)] for m in range(len(nums) + 1)]

# 生成二维前缀和
for i in range(1,len(nums)+1):
    for j in range(1,len(nums[0])+1):
        pre_sum[i][j] = pre_sum[i][j - 1] + pre_sum[i - 1][j] - pre_sum[i - 1][j - 1] + nums[i-1][j-1]

print(pre_sum)
