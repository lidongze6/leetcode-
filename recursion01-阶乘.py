"阶乘"
def factorial(n):
    # for 循环版
    res=1
    for i in range(n,0,-1):
        res*=i
    return res

def factorial_1(n):
    # 递归版
    if n==1:
        return 1
    return n*factorial(n-1)


print(factorial(5))
print(factorial_1(5))
