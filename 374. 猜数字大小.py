class Solution(object):
    """
    The guess API is already defined for you.
    """
    def guessNumber(self, n):
        l,r=1,n
        if l>=r:return l
        while l<r:
            mid=l+(r-l)//2 ## 防止数据溢出
            if guess(mid)==0:return mid
            elif guess(mid)==1:r=mid-1
            else:l=mid+1

        return l

