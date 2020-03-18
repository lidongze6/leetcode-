class NumArray:
    # 前缀和
    def __init__(self, nums: List[int]):
        self.pre_sum=[0]*(len(nums)+1)
        for i in range(1,len(self.pre_sum)):
            self.pre_sum[i]=nums[i-1]+self.pre_sum[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.pre_sum[j+1]-self.pre_sum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)