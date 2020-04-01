class Solution:
    def wiggleMaxLength(self, nums):
        l=len(nums)
        if l<=1:return l
        up=[1]*l # 以i为节点且i是上升阶段的长度
        down=[1]*l # 以i为节点且i是下降阶段的长度
        for i in range(1,l):
            for j in range(i):
                if nums[i]>nums[j]:
                    up[i]=max(up[i],down[j]+1)
                elif nums[i]<nums[j]:
                    down[i]=max(down[i],up[j]+1)
        return max(max(up),max(down))
