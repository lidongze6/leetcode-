def diffWaysToCompute(input):
    if input.isdigit():
        return [int(input)]

    res = []
    for i, char in enumerate(input):
        if char in ['+', '-', '*']:
            # 1.分解：遇到运算符，计算左右两侧的结果集
            # 2.解决：diffWaysToCompute 递归函数求出子问题的解
            left = diffWaysToCompute(input[:i])
            right = diffWaysToCompute(input[i + 1:])
            # 3.合并：根据运算符合并子问题的解
            for l in left:
                for r in right:
                    if char == '+':
                        res.append(l + r)
                    elif char == '-':
                        res.append(l - r)
                    else:
                        res.append(l * r)

    return res


str1 = "2*-1-1"
print(diffWaysToCompute(str1))
