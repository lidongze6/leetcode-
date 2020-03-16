nums=[21,3,45,130,77,71,25,86,60,101,103]

pre_sum=[0 for _ in range(len(nums)+1)]
for i in range(1,len(nums)+1):
    pre_sum[i]=pre_sum[i-1]+nums[i-1]

print(pre_sum)