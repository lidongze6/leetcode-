def fibonacci(n):
    # for 循环版本
    if n==1 or n==2:
        return 1
    a=b=1
    for i in range(2,n):
        a,b=b,a+b
    return b

def fibonacci_1(n):
    # 递归版
    if n==1 or n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)



print(fibonacci(10))
print(fibonacci_1(10))