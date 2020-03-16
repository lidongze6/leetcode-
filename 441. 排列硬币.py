def arrangeCoins(n):
    """
    二分法
    mid为当前的层数，因为每一层的数目也为mid，故到当前层mid的硬币个数为（1+mid)*mid/2
    故只要返回正确的mid即可
    :param n:
    :return:
    """
    l,r=0,n
    while l<r:
        mid=l+(r-l)//2
        sum=(mid+1)*mid/2
        if 0<=n-sum<mid+1:
            return mid
        elif n-sum>=mid+1:
            l=mid+1
        else:r=mid-1
    if l>=r:
        return l
n = 5
print(arrangeCoins(n))