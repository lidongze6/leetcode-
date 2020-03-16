def power(x,n):
    "O(n)"
    if x==1 or n==0:
        return 1
    if n<0:
        return 1/power(x,n)
    if n%2==0:
        return power(x*x,n//2)
    if x%2 !=0:
        return power(x*x,n//2)*x
