def findErrorNums(nums):
    arr=[0]*len(nums)
    for i in range(len(nums)):
        arr[nums[i]-1]+=1
    return [arr.index(2)+1,arr.index(0)+1]