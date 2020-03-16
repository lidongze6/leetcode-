"""
The isBadVersion API is already defined for you.
"""
class Solution:
    def firstBadVersion(self, n):
        self.l,self.r=1,n
        if self.l>=self.r:
            return self.l
        while self.l<self.r:
            mid=(self.l+self.r)//2
            if isBadVersion(mid):
                self.r=mid
            else:
                self.l=mid+1
        return self.l
