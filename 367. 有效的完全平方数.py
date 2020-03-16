def isPerfectSquare(num):
    l,r=1,num
    while l<r:
        mid=(l+r+1)//2
        if mid**2==num:
            return True
        elif mid**2>num:
            r=mid-1
        else:l=mid+1
    if l >= r:
        if l ** 2 == num:
            return True
        else:
            return False


num=16
print(isPerfectSquare(num))


