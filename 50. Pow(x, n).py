def myPow(x, n):
    flag=1
    if n < 0:
        n = abs(n)
        flag=0
    res, tmp = 1, 0
    while tmp < n:
        i, po = 1, x
        while i <= (n - tmp):
            tmp+=i
            res *= po
            po *= po
            i += i

    return res if flag else 1/res

x,n=2.00000, -2
print(myPow(x,n))
