def helper(S):
    # 循环版本
    res=""
    for i in S:
        if i.isalpha():
            res+=i
        elif i.isdigit():
            res*=int(i)
    return res


S = "ha22w4"
K = 10
print(helper(S))
