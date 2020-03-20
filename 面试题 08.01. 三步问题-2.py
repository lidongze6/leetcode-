class Solution:
    def waysToStep(self, n: int):
        # 递归
        if n==1:return 1
        if n==2:return 2
        if n==3:return 4
        return self.waysToStep(n-1)+self.waysToStep(n-2)+self.waysToStep(n-3)


print(Solution().waysToStep(5))