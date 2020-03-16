def mySqrt(x):
    l = 0
    r = x
    while l<r:
        mid=(l+r+1)//2
        if mid**2-x>0:
            r=mid-1
        else:l=mid
    return l


x = 4
print(mySqrt(x))
