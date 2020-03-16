class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # 类似于两数之和的解法
        import collections
        nums=collections.Counter(nums)
        res=0
        if k<0:
            return 0
        if k==0:
            for v in nums.values():
                if v>=2:
                    res+=1
            return res
        for i in nums:
            if i+k in nums:
                res+=1
        return res